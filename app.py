import streamlit as st
import pandas as pd

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
