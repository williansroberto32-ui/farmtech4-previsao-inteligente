
# ==================================================
# FARMTECH 4 - PREVISAO INTELIGENTE
# FIAP - Inteligencia Artificial
# Projeto FarmTech Solutions
# ==================================================

# Etapa 1 - Preparacao do ambiente

import pandas as pd
import numpy as np

print("=" * 50)
print("FARMTECH SOLUTIONS - PREVISAO INTELIGENTE")
print("=" * 50)

print("\nIniciando sistema de analise agricola...")

# Configuracao para reproducibilidade
np.random.seed(42)

print("Ambiente inicial configurado com sucesso!")

# ==================================================
# Etapa 2 - Dados agricolas de exemplo
# ==================================================

dados = pd.DataFrame({
    "umidade": [30, 45, 60, 35, 70, 55, 40, 65, 50, 75],
    "ph": [5.5, 6.0, 6.5, 5.8, 6.8, 6.2, 5.9, 6.7, 6.1, 7.0],
    "irrigacao": [10, 15, 20, 12, 25, 18, 14, 22, 17, 27],
    "fertilizante": [5, 8, 10, 6, 12, 9, 7, 11, 8, 13],
    "produtividade": [20, 30, 42, 25, 50, 38, 28, 46, 35, 53]
})

print("\nDADOS AGRICOLAS:")
print(dados)

print("\nRESUMO ESTATISTICO:")
print(dados.describe())

# ==================================================
# Etapa 3 - Preparacao para Machine Learning
# ==================================================

# Variaveis de entrada
X = dados[["umidade", "ph", "irrigacao", "fertilizante"]]

# Variavel que queremos prever
y = dados["produtividade"]

print("\nVARIAVEIS DE ENTRADA:")
print(X.head())

print("\nVARIAVEL ALVO - PRODUTIVIDADE:")
print(y.head())

print("\nDados preparados para Machine Learning!")

# ==================================================
# Etapa 4 - Treinamento do modelo de regressao
# ==================================================

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Separar dados de treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Criar o modelo
modelo = LinearRegression()

# Treinar a Inteligencia Artificial
modelo.fit(X_treino, y_treino)

print("\nTREINAMENTO DO MODELO:")
print("Modelo de Regressao Linear treinado com sucesso!")

print("\nRegistros para treinamento:", len(X_treino))
print("Registros para teste:", len(X_teste))
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Gerar previsões para os dados de teste
y_previsto = modelo.predict(X_teste)

# Calcular as métricas de desempenho
mae = mean_absolute_error(y_teste, y_previsto)
mse = mean_squared_error(y_teste, y_previsto)
rmse = mse ** 0.5
r2 = r2_score(y_teste, y_previsto)

print("\nAVALIAÇÃO DO MODELO:")
print(f"MAE:  {mae:.2f}")
print(f"MSE:  {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.2f}")
import streamlit as st

st.set_page_config(
    page_title="FarmTech 4 - Previsão Inteligente",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 FarmTech Solutions")
st.subheader("Assistente Agrícola Inteligente")
st.caption("Dashboard demonstrativa com dados agrícolas simulados.")

st.info(
    "A base possui apenas 10 registros simulados. "
    "As previsões e recomendações são demonstrativas."
)

st.subheader("Desempenho do modelo")
col1, col2, col3, col4 = st.columns(4)
col1.metric("MAE", f"{mae:.2f}")
col2.metric("MSE", f"{mse:.2f}")
col3.metric("RMSE", f"{rmse:.2f}")
col4.metric("R²", f"{r2:.2f}")

st.subheader("Dados agrícolas")
st.dataframe(dados)

st.subheader("Relação entre variáveis agrícolas e produtividade")
grafico1, grafico2 = st.columns(2)

with grafico1:
    st.markdown("**Umidade e produtividade**")
    st.scatter_chart(
        dados,
        x="umidade",
        y="produtividade",
        color="ph"
    )

with grafico2:
    st.markdown("**Irrigação e produtividade**")
    st.scatter_chart(
        dados,
        x="irrigacao",
        y="produtividade",
        color="fertilizante"
    )

st.subheader("Simulador de produtividade")
st.caption(
    "Os limites das recomendações são demonstrativos e devem ser ajustados "
    "conforme a cultura e as condições do solo."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    umidade_nova = st.number_input(
        "Umidade (%)", min_value=0, max_value=100, value=50
    )

with col2:
    ph_novo = st.number_input(
        "pH", min_value=0.0, max_value=14.0, value=6.0, step=0.1
    )

with col3:
    irrigacao_nova = st.number_input(
        "Irrigação (valor simulado)", min_value=0, value=15
    )

with col4:
    fertilizante_novo = st.number_input(
        "Fertilizante (valor simulado)", min_value=0, value=8
    )

if st.button("Prever produtividade"):
    novo_cenario = pd.DataFrame({
        "umidade": [umidade_nova],
        "ph": [ph_novo],
        "irrigacao": [irrigacao_nova],
        "fertilizante": [fertilizante_novo]
    })

    previsao = modelo.predict(novo_cenario)[0]
    st.metric("Produtividade prevista", f"{previsao:.2f}")

    if umidade_nova < 40:
        st.warning("Umidade baixa: avalie a necessidade de irrigação.")
    elif umidade_nova >= 70:
        st.info("Umidade elevada: acompanhe o solo antes de irrigar.")
    else:
        st.success("Umidade dentro da faixa usada nesta demonstração.")

    if ph_novo < 5.5 or ph_novo > 7.0:
        st.warning("Confira o pH do solo e as necessidades da cultura.")