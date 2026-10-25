import os

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DW_HOST = os.environ.get("DW_HOST", "localhost")
DW_PORT = os.environ.get("DW_PORT", "5433")
DW_USER = os.environ["DW_USER"]
DW_PASSWORD = os.environ["DW_PASSWORD"]
DW_DATABASE = os.environ["DW_DATABASE"]

engine = create_engine(
    f"postgresql+psycopg2://{DW_USER}:{DW_PASSWORD}@{DW_HOST}:{DW_PORT}/{DW_DATABASE}"
)

st.set_page_config(page_title="BCB Data Platform", layout="wide")
st.title("📊 BCB Data Platform")


@st.cache_data(ttl=600)
def load_cotacoes():
    return pd.read_sql("SELECT * FROM gold.cotacoes_fechamento ORDER BY data_cotacao", engine)


@st.cache_data(ttl=600)
def load_indicadores():
    return pd.read_sql("SELECT * FROM gold.indicadores_economicos ORDER BY data DESC", engine)


cotacoes = load_cotacoes()
indicadores = load_indicadores()

st.subheader("Cotações PTAX (fechamento)")

moedas = sorted(cotacoes["nome_moeda"].dropna().unique())
moeda_selecionada = st.selectbox("Moeda", moedas)

df_moeda = cotacoes[cotacoes["nome_moeda"] == moeda_selecionada].set_index("data_cotacao")
st.line_chart(df_moeda[["cotacaocompra", "cotacaovenda"]])

st.subheader("Indicadores Econômicos")

indicadores_disponiveis = sorted(indicadores["nome_indicador"].dropna().unique())
indicador_selecionado = st.selectbox("Indicador", indicadores_disponiveis)

df_indicador = indicadores[indicadores["nome_indicador"] == indicador_selecionado]
st.line_chart(df_indicador.set_index("data")["valor"])

with st.expander("Ver tabela completa de indicadores"):
    st.dataframe(indicadores, use_container_width=True)
