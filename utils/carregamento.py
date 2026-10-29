import pandas as pd
import streamlit as st

@st.cache_data(ttl=3600)
def carregar_dados(arquivo):

    abax = pd.read_excel(
        arquivo,
        sheet_name="Tabelas Abax"
    )

    comercial = pd.read_excel(
        arquivo,
        sheet_name="Comercial"
    )

    redes = pd.read_excel(
        arquivo,
        sheet_name="Redes"
    )

    base = abax.merge(
        comercial[
            [
                "Cod CDD",
                "D_Base_Loja_GEO[SITE]"
            ]
        ],
        left_on="Comercial",
        right_on="Cod CDD",
        how="left"
    )

    base = base.merge(
        redes[
            [
                "D_Base_Loja_GEO[SITE]",
                "D_Base_Loja_GEO[COD REDE]",
                "D_Base_Loja_GEO[GN]",
                "D_Base_Loja_GEO[SN]"
            ]
        ],
        left_on=[
            "D_Base_Loja_GEO[SITE]",
            "Cod Rede"
        ],
        right_on=[
            "D_Base_Loja_GEO[SITE]",
            "D_Base_Loja_GEO[COD REDE]"
        ],
        how="left"
    )

    return base

