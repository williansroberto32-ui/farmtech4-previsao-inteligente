# FarmTech 4 — Previsão Inteligente

Protótipo didático de um assistente agrícola que usa regressão linear para estimar a produtividade com dados simulados de umidade, pH, irrigação e fertilizante.

## Como funciona

O modelo usa estas variáveis de entrada:

- Umidade
- pH do solo
- Irrigação
- Fertilizante

A variável prevista é a produtividade. O projeto separa os dados em conjuntos de treino e teste e calcula MAE, MSE, RMSE e R².

## Dashboard

A interface feita com Streamlit apresenta:

- Tabela dos dados agrícolas simulados
- Gráficos de relação entre variáveis e produtividade
- Métricas do modelo
- Simulador interativo de produtividade
- Recomendações demonstrativas sobre umidade e pH

## Resultados da execução

A base contém 10 registros simulados: 8 para treino e 2 para teste.

| Métrica | Resultado |
|---|---:|
| MAE | 0,32 |
| MSE | 0,11 |
| RMSE | 0,33 |
| R² | 0,98 |

Como o conjunto de teste tem apenas dois registros simulados, essas métricas são preliminares e não representam desempenho validado em dados reais.

## Como executar

Com Python 3.13 instalado, abra o terminal nesta pasta e execute:

```powershell
py -3.13 -m pip install -r requirements.txt
py -3.13 -m streamlit run main.py