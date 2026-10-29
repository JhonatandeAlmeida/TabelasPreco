import streamlit as st
from utils.carregamento import carregar_dados
from utils.exportacao import exportar_excel

if "arquivo" not in st.session_state:
    st.stop()

df = carregar_dados(st.session_state["arquivo"])

st.title("📋 Consulta")

site = st.multiselect(
    "Site",
    sorted(df["D_Base_Loja_GEO[SITE]"].dropna().unique())
)

if site:
    df = df[
        df["D_Base_Loja_GEO[SITE]"].isin(site)
    ]

c1,c2,c3,c4 = st.columns(4)

c1.metric("Registros", len(df))
c2.metric("Sites", df["D_Base_Loja_GEO[SITE]"].nunique())
c3.metric("Redes", df["Rede"].nunique())
c4.metric("SKUs", df["Cod. SKU"].nunique())

st.dataframe(
    df,
    use_container_width=True,
    height=700
)

st.download_button(
    "📥 Exportar Excel",
    exportar_excel(df),
    "consulta_abax.xlsx"
)
