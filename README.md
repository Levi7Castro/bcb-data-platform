# BCB Data Platform

Plataforma de dados pessoal construída para praticar e demonstrar um stack moderno de Engenharia de Dados, usando como fonte real as APIs públicas do **Banco Central do Brasil (BCB)**: cotações PTAX de câmbio e séries históricas do SGS (Selic, IPCA, IGP-M).

Projeto de portfólio — construído do zero como parte da transição de carreira de Analista de BI para Engenharia de Dados.

## Arquitetura

BCB APIs (SGS, PTAX)
│
▼
Airbyte (PyAirbyte, conector declarativo custom)
│
▼
Postgres — camada BRONZE (dados brutos)
│
▼
dbt — transformações
│
├─▶ SILVER (tipado, testado, documentado)
│
└─▶ GOLD (modelos de negócio, prontos para consumo)
│
▼
Apache Airflow (Astro Runtime) — orquestração do pipeline completo


Todo o ambiente roda em containers Docker, com ambientes Python isolados por ferramenta (Airbyte e dbt têm seus próprios venvs, inclusive dentro da imagem do Airflow) para evitar conflitos de dependências entre eles e com o próprio Airflow.

## Stack técnica

- **Extração:** [PyAirbyte](https://github.com/airbytehq/PyAirbyte) com um conector declarativo (low-code) customizado para as APIs do BCB
- **Armazenamento:** PostgreSQL (camada bronze/silver/gold no mesmo Data Warehouse)
- **Transformação:** [dbt-core](https://www.getdbt.com/) (arquitetura medallion: bronze → silver → gold, com testes genéricos e de negócio, seeds e documentação)
- **Orquestração:** [Apache Airflow](https://airflow.apache.org/) via [Astro CLI](https://www.astronomer.io/docs/astro/cli/overview) / Astro Runtime
- **Containerização:** Docker, com [uv](https://docs.astral.sh/uv/) para gerenciar versões de Python e dependências isoladas
- **CI/CD:** GitHub Actions com separação de ambientes `develop`/`main` *(próxima etapa)*

## Estrutura de pastas

include/
├── airbyte/ # conector declarativo (source_bcb.yaml) e script de carga do bronze
├── dbt/
│ └── bcb_analytics/ # projeto dbt: models/silver, models/gold, seeds, testes
└── airflow/ # projeto Astro: Dockerfile, DAGs, docker-compose.override.yml


## Como rodar localmente

Pré-requisitos: Docker, [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli), Python 3.12+, [uv](https://docs.astral.sh/uv/).

1. Clone o repositório e configure as variáveis de ambiente (credenciais do Postgres).
2. Suba o Postgres do Data Warehouse:
   ```bash
   docker compose up -d
   ```
3. (Opcional, para rodar os scripts fora do Airflow) Crie os venvs isolados do Airbyte e do dbt:
   ```bash
   cd include/airbyte && uv venv --python 3.12 .venv && uv pip install -r requirements.txt
   cd ../dbt && uv venv --python 3.12 .venv && uv pip install -r requirements.txt
   ```
4. Suba o Airflow:
   ```bash
   cd include/airflow
   astro dev start
   ```
5. Acesse a UI do Airflow (`http://airflow.localhost:<porta>`) e dispare a DAG `pipeline_bcb` — ou via CLI:
   ```bash
   astro dev bash -s scheduler -c "airflow dags trigger pipeline_bcb"
   ```

## Roadmap

- [x] Extração das APIs do BCB via PyAirbyte (conector declarativo customizado)
- [x] Carga da camada bronze no Postgres
- [x] Transformações dbt — camada silver (tipada, testada, documentada)
- [x] Transformações dbt — camada gold (modelos de negócio)
- [x] Orquestração completa via Airflow, Dockerizado, com ambientes isolados
- [x] CI/CD com GitHub Actions (separação dev/main, runner self-hosted)
- [x] Dashboard de consumo (Streamlit)

## Autor

**Levi** — Analista de BI / Engenheiro de Dados em transição de carreira, Grupo FAN (Fortaleza, CE).
