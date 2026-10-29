import streamlit as st
import plotly.express as px
from utils.carregamento import carregar_dados

if "arquivo" not in st.session_state:
    st.stop()

st.title("📊 Análise de Preços")

df = carregar_dados(
    st.session_state["arquivo"]
)

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric(
    "Preço Médio",
    round(
        df["Vlr Unit c/ADF Incr"].mean(),
        2
    )
)

c2.metric(
    "Preço Máximo",
    round(
        df["Vlr Unit c/ADF Incr"].max(),
        2
    )
)

c3.metric(
    "Preço Mínimo",
    round(
        df["Vlr Unit c/ADF Incr"].min(),
        2
    )
)

c4.metric(
    "SKUs",
    df["Cod. SKU"].nunique()
)

c5.metric(
    "Redes",
    df["Rede"].nunique()
)

fig1 = px.histogram(
    df,
    x="Vlr Unit c/ADF Incr",
    nbins=40,
    title="Distribuição dos Preços"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

top = (
    df.nlargest(
        20,
        "Vlr Unit c/ADF Incr"
    )
)

fig2 = px.bar(
    top,
    x="Descrição Produto",
    y="Vlr Unit c/ADF Incr",
    color="Rede",
    title="Top 20 Produtos"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
