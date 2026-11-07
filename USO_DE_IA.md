# Declaração de uso de Inteligência Artificial generativa

> **Regra do trabalho:** usar IA generativa é **permitido e incentivado**, mas
> **todo e qualquer uso** precisa estar declarado e detalhado em uma seção própria
> do artigo e na apresentação (vídeo). Uso não declarado é considerado **plágio** e
> leva à **nota zero** no trabalho para todo o grupo.
>
> Este arquivo é o rascunho de trabalho da declaração: preencham **ao longo** do
> projeto (não no último dia) e copiem a tabela para o artigo. Apaguem as linhas de
> exemplo e todas as marcações TODO.

## 1. Ferramentas usadas

| Ferramenta (nome e versão/modelo) | Como acessaram | Quem usou |
|---|---|---|
| Claude (Anthropic), modelo Claude Opus 5.5 | claude.ai, em um Projeto com o enunciado do trabalho e acesso ao repositório do grupo | Zullaê |
| OpenRouter, modelo openai/gpt-6-luna | chave do grupo, via código (`chatbot/llm.py`) | todos (ainda não usado; previsto para as respostas do bot e a geração de frases de treino) |

## 2. Usos, um por linha

| # | Etapa | O que a IA fez | Prompt (ou resumo + link para o registro) | O que o grupo fez com o resultado |
|---|---|---|---|---|
| 1 | Entendimento do trabalho | Resumiu o enunciado (`Trabalho 1.pdf`), explicou os requisitos e sugeriu um cronograma até 18/11 | "me ajude a entender o trabalho e como realizá-lo" | Usamos o resumo para dividir as tarefas; conferimos os requisitos no próprio enunciado |
| 2 | Domínio e intenções (`grupo.yaml`) | A partir das ideias iniciais do grupo (orientador, prazos, banca, formatação, dilação), sugeriu nomes válidos, juntar "dilação" com "prazos" e acrescentar `inicio_tcc`; redigiu as respostas fixas das 6 intenções com base na Res. 595-Cograd/UFMS e no manual de TCC da FACOM | "me ajude a construir [o grupo.yaml], me dê o passo a passo" | Aceitamos as 6 intenções; mantivemos a persona e as descrições escritas pelo grupo; conferimos as respostas fixas com os dois documentos oficiais |
| 3 | Configuração | Pesquisou e indicou os e-mails institucionais da FACOM para o campo `contato` | "ache o contato de email do coordenador"| Escolhemos o e-mail geral da FACOM (facom@ufms.br), porque o bot atende alunos de vários cursos |
| 4 | Base de conhecimento | Localizou a Res. 595-Cograd/UFMS e o manual de TCC da FACOM; redigiu os 7 guias `.md` da pasta `documentos/` (um por intenção + FAQ geral) e o `FONTES.md` | "vamos prosseguir" (próximo passo: pasta `documentos/`) | Baixamos os 2 PDFs oficiais; testamos a busca com `scripts/indexar_documentos.py --buscar`; os guias estão declarados no `FONTES.md` como escritos com ajuda de IA |
| 5 | Depuração | Identificou que o código-base só reconhece títulos Markdown seguidos de linha em branco (sem ela, os guias perdiam quase todo o texto no índice)| pedido para conferir a indexação dos documentos | Conferimos o resumo do índice antes e depois (de ~150 para todo o texto de cada guia) |
| 6 | Git | Explicou a instalação do ambiente (`.venv`, `requirements.txt`) |

## 3. O que NÃO foi feito com IA

- Escolha do tema (TCC) e a proposta enviada ao professor.
- Ideias iniciais das intenções e a persona do bot (Brunao), escritas pelo grupo.
- Download dos documentos oficiais (Res. 595-Cograd e manual da FACOM).
- Previsto: as frases do conjunto de teste (formulário respondido por pessoas de fora do grupo), a análise dos erros e as conclusões do artigo.

## 4. Reflexão (2 a 4 frases)

Até aqui, a IA ajudou a entender o enunciado, a encontrar os documentos oficiais e a transformar as regras em respostas e guias, o que adiantou bastante o trabalho. Ela errou ao formatar os guias de um jeito que o código-base não lia direito; descobrimos isso testando a busca com `indexar_documentos.py`. Por isso verificamos cada resposta fixa e cada guia contra os documentos oficiais e testamos tudo com os scripts do repositório antes de commitar.
