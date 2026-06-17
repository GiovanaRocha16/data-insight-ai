import pandas as pd
import matplotlib.pyplot as plt


def carregar_dados():
    return pd.read_csv("data/vendas.csv")


def analisar_dados(dados):
    media = dados["Vendas"].mean()
    maior = dados["Vendas"].max()
    menor = dados["Vendas"].min()

    mes_maior = dados.loc[dados["Vendas"].idxmax(), "Mes"]
    mes_menor = dados.loc[dados["Vendas"].idxmin(), "Mes"]

    return media, maior, menor, mes_maior, mes_menor


def plotar_grafico(dados):
    plt.plot(dados["Mes"], dados["Vendas"])
    plt.title("Vendas por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Vendas")
    plt.show()


def main():
    dados = carregar_dados()

    media, maior, menor, mes_maior, mes_menor = analisar_dados(dados)

    print("=== ESTATÍSTICAS ===")
    print("Média:", media)
    print("Maior venda:", maior)
    print("Menor venda:", menor)

    print("\n=== INSIGHTS ===")
    print("Melhor mês:", mes_maior)
    print("Pior mês:", mes_menor)

    primeira = dados["Vendas"].iloc[0]
    ultima = dados["Vendas"].iloc[-1]

    variacao = ((ultima - primeira) / primeira) * 100

    if variacao > 0:
        print(f"\n📈 Crescimento de {variacao:.2f}% no período")
    else:
        print(f"\n📉 Queda de {variacao:.2f}% no período")

    plotar_grafico(dados)

    with open("relatorio.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE VENDAS\n\n")
        f.write("=== ESTATÍSTICAS ===\n")
        f.write(f"Média: {media}\n")
        f.write(f"Maior venda: {maior}\n")
        f.write(f"Menor venda: {menor}\n\n")

        f.write("=== INSIGHTS ===\n")
        f.write(f"Melhor mês: {mes_maior}\n")
        f.write(f"Pior mês: {mes_menor}\n\n")

        f.write(f"Variação no período: {variacao:.2f}%\n")

if __name__ == "__main__":
    main()