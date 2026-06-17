import pandas as pd

dados = pd.read_csv("data/vendas.csv")

print("=== DADOS ===")
print(dados)

print("\n=== ESTATÍSTICAS ===")
print("Média:", dados["Vendas"].mean())
print("Maior venda:", dados["Vendas"].max())
print("Menor venda:", dados["Vendas"].min())