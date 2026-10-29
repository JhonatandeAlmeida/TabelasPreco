import streamlit as st
import plotly.express as px
from utils.carregamento import carregar_dados

if "arquivo" not in st.session_state:
    st.stop()

st.title("🌎 Mapa Comercial")

df = carregar_dados(
    st.session_state["arquivo"]
)

fig = px.sunburst(
    df,
    path=[
        "D_Base_Loja_GEO[SITE]",
        "D_Base_Loja_GEO[GN]",
        "D_Base_Loja_GEO[SN]",
        "Rede"
    ]
)

st.plotly_chart(
    fig,
    use_container_width=True
)
