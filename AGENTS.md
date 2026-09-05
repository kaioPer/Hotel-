# AGENTS.md

## Stack
- Backend: Python + Flask + Flask-CORS
- Agente IA: Agno (`gpt-4o-mini` via `agno.models.openai.OpenAIChat`)
- Banco de dados: Supabase (tabela `reservas`)
- Frontend: HTML/CSS/JS estático servido pelo Flask

## Estrutura
- `app.py` — único backend: rotas `/`, `/perguntar`, `/reservas` (POST e GET)
- `static/index.html` — frontend completo (chat + reserva), servido por `app.send_static_file`
- Não há `requirements.txt` nem build do frontend; dependências vivem apenas em `.venv`

## Como rodar
- Ativar venv: `.venv\Scripts\Activate.ps1`
- Rodar servidor: `python app.py`
- Servidor sobe em `http://0.0.0.0:8000` com `debug=True`
- O app exige no `.env`: `SUPABASE_URL`, `SUPABASE_KEY` e `OPENAI_API_KEY`
- O `.venv` usa **Python 3.14.7** (agno 3.x, flask, supabase, python-dotenv)

## Endpoints
- `POST /perguntar` — body JSON `{"pergunta": "..."}`, retorna `{"mensagem": ...}`
- `POST /reservas` — body JSON com `nome`, `quarto`, `checkin`, `checkout`; insere na tabela `reservas`
- `GET /reservas` — retorna lista de reservas

## Gotchas
- NÃO alterar a `description` do agente (app.py linha ~23) — é railguard explícito
- O frontend (`index.html`) exibe preços/nomes de quartos DIFERENTES da `description` do agente (ex.: "Suíte Presidencial" vs "Quarto Luxo"). É intencional/em aberto; não "corrigir" a descrição para bater com o HTML
- Nada de testes, lint ou typecheck configurado no repo
- A raiz do git é a pasta pai (`Caio Peruchi Rodrigues`), que reúne vários projetos irmãos; este projeto não tem commits próprios — cuidado ao commitar para não incluir arquivos de outros projetos

## Railguards
- Não alterar a lógica do projeto
- Não alterar/criar arquivos sem pedir autorização
- Não instalar bibliotecas desnecessárias
- Não expor/ler arquivos `.env` e `.gitignore`
- Não alterar a `description` do agente de hotel

## Preferências
- Responder sempre em PT-BR
- Comentar o código, pensando em programador iniciante
