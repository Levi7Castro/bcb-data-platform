## Pré-requisitos

- Docker e Docker Compose
- Python 3.12
- [uv](https://docs.astral.sh/uv/) instalado

## Configuração local

\`\`\`bash
cp .env.example .env          # edite com suas credenciais
docker compose up -d          # sobe o Postgres do DW

uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -r include/airbyte/requirements.txt
\`\`\`# bcb-data-platform
