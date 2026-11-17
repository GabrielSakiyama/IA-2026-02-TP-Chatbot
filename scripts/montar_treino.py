#!/usr/bin/env python3
"""Monta o dados/treino.csv a partir das fontes do grupo.

Classe por classe, até o mínimo do enunciado, nesta ordem de prioridade:

  1. frases humanas: todos os dados/humano_*.csv (entram todas);
  2. frases do LLM: dados/gerados_llm_revisado.csv (enquanto a revisão não
     existe, usa dados/gerados_llm.csv e avisa que o treino é provisório);
  3. MASSIVE, só para completar o fora_dominio. O chitchat do MASSIVE não entra:
     lá pedido de piada é chitchat, mas o enunciado trata como fora_dominio.

Frases repetidas entre as fontes (ignorando maiúsculas, acentos e pontuação)
entram uma vez só, valendo a humana.

Pela regra dos 20%, com H frases humanas o treino pode ter no máximo 5 x H
frases. O script avisa se a conta não fechar.

Uso:
    python scripts/montar_treino.py
    python scripts/montar_treino.py --por-intencao 60 --chitchat 100 --fora 150
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from chatbot.config import carregar_config  # noqa: E402
from chatbot.dados import COLUNAS, carregar_dados, validar_dados  # noqa: E402
from chatbot.texto import normalizar  # noqa: E402

HUMANAS = {"humano", "coletado"}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--por-intencao", type=int, default=50, help="frases por intenção do domínio")
    ap.add_argument("--chitchat", type=int, default=100)
    ap.add_argument("--fora", type=int, default=150)
    ap.add_argument("--semente", type=int, default=42)
    args = ap.parse_args(argv)

    config = carregar_config(RAIZ / "grupo.yaml")
    dados = RAIZ / "dados"
    revisado = dados / "gerados_llm_revisado.csv"

    humanas = pd.concat([carregar_dados(p) for p in sorted(dados.glob("humano_*.csv"))], ignore_index=True)
    llm = carregar_dados(revisado if revisado.exists() else dados / "gerados_llm.csv")
    massive = carregar_dados(dados / "geral" / "massive_fora_dominio.csv")

    alvos = {nome: args.por_intencao for nome in config.nomes_intencoes}
    alvos["chitchat"] = args.chitchat
    alvos["fora_dominio"] = args.fora

    usados: set[str] = set()

    def sem_repetidas(df: pd.DataFrame) -> pd.DataFrame:
        chave = df["texto"].map(normalizar)
        return df[~chave.isin(usados) & ~chave.duplicated()]

    humanas = sem_repetidas(humanas)
    usados.update(humanas["texto"].map(normalizar))
    partes = [humanas]

    for rotulo, alvo in alvos.items():
        falta = alvo - int((humanas["intencao"] == rotulo).sum())
        fontes = [llm, massive] if rotulo == "fora_dominio" else [llm]
        for fonte in fontes:
            if falta <= 0:
                break
            candidatas = sem_repetidas(fonte[fonte["intencao"] == rotulo])
            escolhidas = candidatas.sample(n=min(falta, len(candidatas)), random_state=args.semente)
            usados.update(escolhidas["texto"].map(normalizar))
            partes.append(escolhidas)
            falta -= len(escolhidas)
        if falta > 0:
            print(f"[AVISO] {rotulo}: faltam {falta} frases para chegar em {alvo}")

    treino = pd.concat(partes, ignore_index=True)[COLUNAS]
    problemas = validar_dados(treino, config)
    if problemas:
        print("[ERRO] treino inválido:", problemas)
        return 1
    treino.to_csv(dados / "treino.csv", index=False)

    print(pd.crosstab(treino["intencao"], treino["origem"], margins=True, margins_name="total"))
    n_humanas = int(treino["origem"].isin(HUMANAS).sum())
    print(f"\nfrases humanas: {n_humanas} de {len(treino)} ({n_humanas / len(treino):.1%}); "
          f"com {n_humanas} humanas, o treino pode ter no máximo {5 * n_humanas} frases")
    if n_humanas / len(treino) < 0.20:
        print("[AVISO] menos de 20% de frases humanas: o verificar_entrega.py vai acusar ERRO")
    if not revisado.exists():
        print("[AVISO] treino PROVISÓRIO: usa dados/gerados_llm.csv sem revisão. "
              "Salve a revisão em dados/gerados_llm_revisado.csv e rode de novo.")
    print(f"\n{len(treino)} frases gravadas em {dados / 'treino.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
