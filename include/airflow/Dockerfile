FROM astrocrpublic.azurecr.io/runtime:3.3-11

# Ambiente isolado para o conector Airbyte (Python 3.12 — o pacote airbyte ainda não suporta o 3.14 da imagem base)
# --no-config evita que o uv aplique a constraint global de SQLAlchemy==2.0.50 do Airflow (definida em /pyproject.toml)
RUN uv python install 3.12 && \
    uv venv --python 3.12 /usr/local/airflow/venvs/airbyte && \
    uv pip install --no-config --python /usr/local/airflow/venvs/airbyte/bin/python \
        airbyte==0.35.7 \
        sqlalchemy==2.0.37 \
        psycopg2-binary==2.9.10 \
        pyyaml==6.0.2

# Ambiente isolado para o dbt (mesma versão de Python, por consistência)
RUN uv venv --python 3.12 /usr/local/airflow/venvs/dbt && \
    uv pip install --no-config --python /usr/local/airflow/venvs/dbt/bin/python \
        dbt-core==1.9.4 \
        dbt-postgres==1.9.1
