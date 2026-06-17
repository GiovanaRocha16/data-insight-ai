import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_insight_ia(dados):
    return "IA temporariamente desativada (sem crédito na API)"

st.set_page_config(page_title="Data Insight AI", layout="wide")

st.title("📊 Data Insight AI")

dados = pd.read_csv("data/vendas.csv")

mes_selecionado = st.selectbox(
    "📅 Selecione o mês",
    dados["Mes"].unique()
)

dados_filtrados = dados[dados["Mes"] == mes_selecionado]

st.subheader("📁 Dados completos")
st.dataframe(dados)

st.subheader("📊 Estatísticas do mês selecionado")

st.write("📅 Mês:", mes_selecionado)
st.write("💰 Venda:", dados_filtrados["Vendas"].values[0])

st.subheader("📈 Evolução das vendas (geral)")
st.line_chart(dados.set_index("Mes"))

st.subheader("📊 Destaque do mês selecionado")
st.bar_chart(dados_filtrados.set_index("Mes"))

st.subheader("🤖 IA de Insights")

if st.button("Gerar análise com IA"):
    with st.spinner("Analisando dados com IA..."):
        insight = gerar_insight_ia(dados)
        st.success("Análise gerada!")
        st.write(insight)