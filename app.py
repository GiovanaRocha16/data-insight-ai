import streamlit as st
import pandas as pd

st.title("📊 Data Insight AI")

dados = pd.read_csv("data/vendas.csv")

st.subheader("📁 Dados")
st.dataframe(dados)

st.subheader("📈 Estatísticas")
st.write("Média:", dados["Vendas"].mean())
st.write("Maior venda:", dados["Vendas"].max())
st.write("Menor venda:", dados["Vendas"].min())

st.subheader("📊 Gráfico")
st.line_chart(dados.set_index("Mes"))