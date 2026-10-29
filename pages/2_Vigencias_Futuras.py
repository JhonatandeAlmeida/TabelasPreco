import streamlit as st
import pandas as pd
import plotly.express as px
from utils.carregamento import carregar_dados
from utils.filtros import aplicar_filtros_globais

arquivo = arquivo = st.session_state.get("arquivo")

df = carregar_dados()

df = aplicar_filtros_globais(df)

st.title("📅 Vigências Futuras")

df["Vigência INI"] = pd.to_datetime(
    df["Vigência INI"]
)

grupo = [
    "D_Base_Loja_GEO[SITE]",
    "Rede",
    "UF Origem",
    "UF Destino",
    "Cod. SKU"
]

impactados = (
    df.groupby(grupo)
    ["Vigência INI"]
    .nunique()
    .reset_index()
)

impactados = impactados[
    impactados["Vigência INI"] > 1
]

st.metric(
    "SKUs com Vigência Futura",
    len(impactados)
)

st.dataframe(
    impactados,
    use_container_width=True
)

grafico = (
    impactados
    .groupby("Rede")
    .size()
    .reset_index(name="Qtde")
)

fig = px.bar(
    grafico,
    x="Rede",
    y="Qtde",
    title="Impactos por Rede"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
