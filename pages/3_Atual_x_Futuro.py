import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils.carregamento import carregar_dados
from utils.filtros import aplicar_filtros_globais

if "arquivo" not in st.session_state:
    st.stop()

st.title("🔄 Atual x Futuro")

df = carregar_dados(
    st.session_state["arquivo"]
)

df = aplicar_filtros_globais(df)

df["Vigência INI"] = pd.to_datetime(
    df["Vigência INI"]
)

df = df.sort_values(
    "Vigência INI"
)

comparativo = []

for _, grp in df.groupby(
    [
        "D_Base_Loja_GEO[SITE]",
        "Rede",
        "Cod. SKU"
    ]
):

    if len(grp) < 2:
        continue

    atual = grp.iloc[0]
    futuro = grp.iloc[-1]

    comparativo.append({
        "Site": atual["D_Base_Loja_GEO[SITE]"],
        "Rede": atual["Rede"],
        "SKU": atual["Cod. SKU"],
        "Preço Atual": atual["Vlr Unit c/ADF Incr"],
        "Preço Futuro": futuro["Vlr Unit c/ADF Incr"]
    })

comp = pd.DataFrame(comparativo)

if len(comp):

    comp["Dif R$"] = (
        comp["Preço Futuro"]
        - comp["Preço Atual"]
    )

    comp["Dif %"] = (
        comp["Dif R$"]
        / comp["Preço Atual"]
    ) * 100

    st.dataframe(
        comp,
        use_container_width=True
    )
