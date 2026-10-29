import streamlit as st

st.set_page_config(
    page_title="ABAX Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Consolidador ABAX")

arquivo = "data/Consolidador Abax.xlsx"

if arquivo:
    st.session_state["arquivo"] = arquivo
    st.success("Arquivo carregado.")
else:
    st.info("Selecione um arquivo para iniciar.")
