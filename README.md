# 📊 Data Insight AI

Projeto de análise de dados com Python e Streamlit, que transforma dados de vendas em insights automáticos e visualizações interativas.

---

## 🚀 Resumo

O projeto analisa um conjunto de dados de vendas mensais e gera:

- 📈 Estatísticas automáticas
- 📊 Gráfico de evolução
- 📄 Relatório em arquivo
- 🌐 Dashboard interativo

---

## 🧠 Funcionalidades

- Leitura de dados CSV com Pandas
- Cálculo de métricas:
  - Média
  - Maior valor
  - Menor valor
- Identifica:
  - Melhor mês
  - Pior mês
  - Tendência de crescimento
- Geração de relatório automático (.txt)
- Interface web com Streamlit
- Visualização gráfica com Matplotlib

---

## 🛠️ Tecnologias

- Python
- Pandas
- Matplotlib
- Streamlit
- Git & GitHub

---

## 📊 Como executar o projeto

```bash
# instalar dependências
pip install -r requirements.txt

# rodar versão terminal
python main.py

# rodar dashboard web
python -m streamlit run app.py
```

---

## 📂 Estrutura do projeto

```text
data-insight-ai/
│
├── app.py              # dashboard Streamlit
├── main.py             # versão análise em terminal
├── data/               # dados CSV
├── relatorio.txt       # relatório gerado
├── requirements.txt    # dependências
└── README.md
```

---

## 🚀 Status

- ✔ Projeto funcional  
- 🚧 Em evolução