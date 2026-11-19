# Declaração de uso de Inteligência Artificial generativa

> **Regra do trabalho:** usar IA generativa é **permitido e incentivado**, mas
> **todo e qualquer uso** precisa estar declarado e detalhado em uma seção própria
> do artigo e na apresentação (vídeo). Uso não declarado é considerado **plágio** e
> leva à **nota zero** no trabalho para todo o grupo.
>
> Este arquivo é o rascunho de trabalho da declaração: preencham **ao longo** do
> projeto (não no último dia) e copiem a tabela para o artigo. Apaguem as linhas de
> exemplo e todas as marcações.

## 1. Ferramentas usadas

| Ferramenta (nome e versão/modelo) | Como acessaram | Quem usou |
|---|---|---|
| Claude (Anthropic), modelo Claude Opus 5.5 | claude.ai, em um Projeto com o enunciado do trabalho e acesso ao repositório do grupo; extensão Claude in Chrome para montar o formulário de teste | Zullaê |
| Claude (Anthropic), modelo Claude Opus 5.5 | Claude Code (app desktop), com acesso à pasta local do repositório | Natan |
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
| 8 | Dados de teste | Montou no Google Forms (conta institucional do Zullaê, pelo navegador) o formulário de coleta das frases de teste: título, descrição e 9 perguntas (uma por intenção, uma opcional, outros assuntos e cumprimentos), a partir do texto sugerido por ela mesma e aprovado pelo grupo | "crie o formulário, use meu e-mail institucional" | Conferimos as perguntas e as configurações, e nós mesmos publicamos e divulgamos o formulário; as frases do teste serão escritas pelos participantes, não pela IA |
| 9 | Ambiente (Passo 1) | Localizou o enunciado e a cópia atualizada do repositório; explicou o ambiente virtual e o `requirements.txt`; diagnosticou a falha do `python -m venv` (faltava o pacote `python3.14-venv` no Ubuntu) e criou o `.venv` com `virtualenv`; instalou as dependências e conferiu as importações e a leitura do `grupo.yaml` | Natan pediu para seguir a Seção 4 do enunciado um passo por vez, explicando o conceito e cada comando antes de rodar | A PREENCHER (Natan) |
| 10 | Chave do OpenRouter (Passo 2) | Conferiu, sem ler a chave, que o `.env` ainda estava igual ao modelo e que o Git o ignora; rodou `scripts/testar_llm.py` com a chave mascarada na saída e explicou o resultado; detectou os backups `.env.save*` do nano (um deles com a chave) antes do commit e os adicionou ao `.gitignore` | pedido para testar a chave sem mostrá-la | Natan colou a chave no `.env` ele mesmo e apagou os backups; a chave não foi copiada para nenhum outro lugar |
| 11 | Dados de treino (Passo 6) | Diagnosticou e corrigiu um erro do `scripts/baixar_massive.py` com o pandas 3 (o `groupby().apply` descartava a coluna `massive_intencao`; trocado por `groupby().sample`) | "pode" rodar o `baixar_massive.py` e o `gerar_dados_llm.py` | Natan autorizou a execução dos dois scripts; a correção é de 2 linhas e está comentada no script |
| 12 | Dados de treino (Passo 6) | OpenRouter, `openai/gpt-6-luna`, via `scripts/gerar_dados_llm.py`: gerou 499 frases candidatas (50 por intenção, 99 de chitchat e 100 de fora_dominio) em 5 estilos, gravadas em `dados/gerados_llm.csv` com `origem = llm`; 40 chamadas, 5.877 tokens de entrada e 12.715 de saída (cerca de US$ 0,007) | os 40 prompts estão registrados em `dados/prompts_llm.md` | Revisão com triagem do Claude (ver #17): 28 descartadas e 1 rótulo corrigido, das 499; 380 entraram no `treino.csv` (as demais ficaram de reserva em `dados/gerados_llm_revisado.csv`) |
| 13 | Dados de treino (Passo 6) | Propôs "situações" (cenários de aluno) para guiar a escrita das frases humanas do Natan, sem escrever as frases; sugeriu o rótulo de cada frase, apontou ambiguidades (ex.: uma frase pedida para `orientador` que perguntava "como começar" foi rotulada `inicio_tcc`) e salvou em `dados/humano_natan.csv`, conferindo com `validar_dados` | Natan respondia às situações no chat, com as próprias palavras | As frases foram escritas pelo Natan; até aqui ele não alterou nenhum dos rótulos sugeridos |
| 14 | Dados de treino (Passo 6) | Escreveu `scripts/montar_treino.py`, que junta as frases humanas, as do LLM e as do MASSIVE até o mínimo de cada classe, remove repetidas entre as fontes e confere a regra dos 20%; extraiu do PDF da planilha as 45 frases do Zullaê para `dados/humano_planilha.csv` (provisório, até a exportação em CSV) | pedido para montar um treino provisório enquanto a revisão do LLM e as frases do Gabriel não chegam | A PREENCHER (Natan) |
| 15 | Análise exploratória (Passo 7) | Escreveu a célula de análise exploratória da seção 2 do `notebooks/01_trabalho_grupo.ipynb` (tamanho médio das mensagens por escopo e origem, termos de maior TF-IDF médio por rótulo, contagem e exemplos de negativos difíceis) e explicou os resultados | pedido para fazer o Passo 7 junto, explicando o conceito | A PREENCHER (Natan) |
| 16 | Primeiro classificador (Passo 8) | Treinou o pipeline da Seção 3.4 do enunciado (TF-IDF de caracteres + regressão logística) com o treino provisório, mostrou as probabilidades para 5 frases de teste rápido e quais pedaços de texto pesaram na decisão | as 5 frases de teste rápido foram escritas pelo Natan (não entram em nenhum arquivo de dados) | A PREENCHER (Natan) |
| 17 | Revisão das frases do LLM (Passo 6) | Leu as 499 frases geradas e marcou 29 suspeitas: 16 artificiais (ex.: "banca de disciplinas", "orientador pra começar a correr"), 12 ambíguas (ex.: "Até quando posso enviar?", "projeto de pesquisa", que serve para TCC e para IC) e 1 com rótulo errado; considerou as outras 470 aceitáveis; gravou o resultado em `dados/gerados_llm_revisado.csv` | revisão conjunta: o Claude marca as suspeitas, o Natan decide | Natan aceitou as 29 sugestões (28 apagadas, 1 rótulo corrigido de `banca` para `chitchat`) e observou que parte das ambíguas seria compreensível com o contexto da conversa, que o classificador (uma mensagem por vez) não usa |
| 18 | Rótulos das frases humanas (Passo 6) | Conferiu os rótulos das 90 frases da planilha (Zullaê e Gabriel) e apontou 5 suspeitos: 2 de `banca` que são `deposito`, 1 de `inicio_tcc` que é `prazos`, 1 de `prazos` que é `inicio_tcc` e 1 ambígua | conferência feita junto da montagem do treino | Natan aprovou as 5 correções (4 rótulos trocados, 1 frase apagada) |
| 19 | Dados de teste | Sugeriu o rótulo das 195 frases das 19 respostas do formulário, apontou 29 para descarte (sem intenção, não eram perguntas, repetidas, ambíguas ou já presentes no treino) e conferiu que nenhuma frase do teste estava no treino | “olhe a planilha” | Zullaê revisou os rótulos; as frases complementares da aba teste foram escritas pelo Zullaê |
| 20 | Comparação de algoritmos (Passo 9) | Acrescentou ao notebook a representação TF-IDF de palavras sem palavras vazias (lista própria, mantendo as palavras de pergunta) e os classificadores KNN e Naive Bayes; rodou a comparação do classificador de escopo (15 combinações, validação cruzada com 5 folds) e explicou os resultados, incluindo a matriz de confusão do Naive Bayes | Natan pediu para acrescentar as variações sugeridas | A PREENCHER (Natan) |
| 21 | Ajuste do escopo (Passo 10) | Escreveu no notebook a grade do `GridSearchCV` (C de 0,01 a 1000, `class_weight` e tamanho dos n-gramas), a célula da curva de validação e o texto que registra a escolha do grupo; rodou e explicou os resultados | Natan escolheu a regressão logística ("vai no mais simples") entre os dois modelos empatados | A PREENCHER (Natan) |
| 22 | Conferência do teste (Passo 6) | Conferiu o `dados/teste.csv` do Zullaê com as funções do código-base: formato, mínimos por classe e ausência de frases do treino (vazamento); o conteúdo não foi usado para escolher modelos | pedido para ver o commit do Zullaê | A PREENCHER (Natan) |
| 23 | Erros do escopo (Passo 11) | Completou a célula de análise de erros do notebook (taxas de falso aceite e falsa recusa, erros por origem), rodou e agrupou os erros por tipo para discussão | pedido para fazer o Passo 11 junto | Natan decidiu que o falso aceite é o erro mais grave no bot de TCC: responder com confiança sobre outro assunto confunde o usuário e pode causar erros graves |

## 3. O que NÃO foi feito com IA

- Escolha do tema (TCC) e a proposta enviada ao professor.
- Ideias iniciais das intenções e a persona do bot (Brunao), escritas pelo grupo.
- Download dos documentos oficiais (Res. 595-Cograd e manual da FACOM).
- Previsto: as frases do conjunto de teste (formulário respondido por pessoas de fora do grupo), a análise dos erros e as conclusões do artigo.

## 4. Reflexão (2 a 4 frases)

Até aqui, a IA ajudou a entender o enunciado, a encontrar os documentos oficiais e a transformar as regras em respostas e guias, o que adiantou bastante o trabalho. Ela errou ao formatar os guias de um jeito que o código-base não lia direito; descobrimos isso testando a busca com `indexar_documentos.py`. Por isso verificamos cada resposta fixa e cada guia contra os documentos oficiais e testamos tudo com os scripts do repositório antes de commitar.
