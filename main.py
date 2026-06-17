import pandas as pd

dados = pd.read_csv("data/vendas.csv")

print("=== DADOS ===")
print(dados)

print("\n=== ESTATÍSTICAS ===")
print("Média:", dados["Vendas"].mean())
print("Maior venda:", dados["Vendas"].max())
print("Menor venda:", dados["Vendas"].min())

mes_maior_venda = dados.loc[dados["Vendas"].idxmax(), "Mes"]
mes_menor_venda = dados.loc[dados["Vendas"].idxmin(), "Mes"]

print("\n=== INSIGHTS ===")
print(f"Melhor mês: {mes_maior_venda}")
print(f"Pior mês: {mes_menor_venda}")

primeira_venda = dados["Vendas"].iloc[0]
ultima_venda = dados["Vendas"].iloc[-1]

if ultima_venda > primeira_venda:
    print("Tendência: crescimento 📈")
elif ultima_venda < primeira_venda:
    print("Tendência: queda 📉")
else:
    print("Tendência: estabilidade ➡️")