import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Consolidador Abax",
    layout="wide"
)

@st.cache_data
def carregar_dados(arquivo):

    df_abax = pd.read_excel(
        arquivo,
        sheet_name="Tabelas Abax"
    )

    df_comercial = pd.read_excel(
        arquivo,
        sheet_name="Comercial"
    )

    df_redes = pd.read_excel(
        arquivo,
        sheet_name="Redes"
    )

    return df_abax, df_comercial, df_redes


arquivo = "data/Consolidador Abax.xlsx"

if arquivo:

    abax, comercial, redes = carregar_dados(arquivo)

    # Relacionamento 1
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

    # Relacionamento 2
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

    tabela_final = base[
        [
            "D_Base_Loja_GEO[SITE]",
            "Rede",
            "D_Base_Loja_GEO[GN]",
            "D_Base_Loja_GEO[SN]",
            "Vigência INI",
            "UF Origem",
            "UF Destino",
            "Cod. SKU",
            "Descrição Produto",
            "Valor C/ Prazo Adic.",
            "Vlr Unit c/ADF Incr"
        ]
    ].copy()

    st.title("Consolidador ABAX")

    col1, col2, col3 = st.columns(3)

    lista_site = sorted(
        tabela_final["D_Base_Loja_GEO[SITE]"]
        .dropna()
        .unique()
    )

    lista_uf = sorted(
        tabela_final["UF Destino"]
        .dropna()
        .unique()
    )

    site = col1.multiselect(
        "Site",
        lista_site
    )

    uf = col2.multiselect(
        "UF Destino",
        lista_uf
    )

    rede = col3.multiselect(
        "Rede",
        sorted(
            tabela_final["Rede"]
            .dropna()
            .unique()
        )
    )

    filtro = tabela_final.copy()

    if site:
        filtro = filtro[
            filtro["D_Base_Loja_GEO[SITE]"].isin(site)
        ]

    if uf:
        filtro = filtro[
            filtro["UF Destino"].isin(uf)
        ]

    if rede:
        filtro = filtro[
            filtro["Rede"].isin(rede)
        ]

    st.metric(
        "Registros",
        len(filtro)
    )

    st.dataframe(
        filtro,
        use_container_width=True,
        height=700
    )

    csv = filtro.to_csv(
        index=False,
        sep=";"
    ).encode("utf-8-sig")

    st.download_button(
        "Exportar CSV",
        csv,
        "abax.csv",
        "text/csv"
    )
