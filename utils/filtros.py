import streamlit as st


def aplicar_filtros_globais(df):

    st.sidebar.header("Filtros Globais")

    if st.sidebar.button(
        "🔄 Limpar Filtros"
    ):
        st.rerun()

    site = st.sidebar.multiselect(
        "Site",
        sorted(
            df["D_Base_Loja_GEO[SITE]"]
            .dropna()
            .unique()
        )
    )

    rede = st.sidebar.multiselect(
        "Rede",
        sorted(
            df["Rede"]
            .dropna()
            .unique()
        )
    )

    gn = st.sidebar.multiselect(
        "GN",
        sorted(
            df["D_Base_Loja_GEO[GN]"]
            .dropna()
            .unique()
        )
    )

    sn = st.sidebar.multiselect(
        "SN",
        sorted(
            df["D_Base_Loja_GEO[SN]"]
            .dropna()
            .unique()
        )
    )

    uf_origem = st.sidebar.multiselect(
        "UF Origem",
        sorted(
            df["UF Origem"]
            .dropna()
            .unique()
        )
    )

    uf_destino = st.sidebar.multiselect(
        "UF Destino",
        sorted(
            df["UF Destino"]
            .dropna()
            .unique()
        )
    )

    sku = st.sidebar.multiselect(
        "SKU",
        sorted(
            df["Cod. SKU"]
            .dropna()
            .unique()
        )
    )

    produto = st.sidebar.text_input(
        "Descrição Produto"
    )

    if site:
        df = df[
            df["D_Base_Loja_GEO[SITE]"]
            .isin(site)
        ]

    if rede:
        df = df[
            df["Rede"]
            .isin(rede)
        ]

    if gn:
        df = df[
            df["D_Base_Loja_GEO[GN]"]
            .isin(gn)
        ]

    if sn:
        df = df[
            df["D_Base_Loja_GEO[SN]"]
            .isin(sn)
        ]

    if uf_origem:
        df = df[
            df["UF Origem"]
            .isin(uf_origem)
        ]

    if uf_destino:
        df = df[
            df["UF Destino"]
            .isin(uf_destino)
        ]

    if sku:
        df = df[
            df["Cod. SKU"]
            .isin(sku)
        ]

    if produto:
        df = df[
            df["Descrição Produto"]
            .astype(str)
            .str.contains(
                produto,
                case=False,
                na=False
            )
        ]

    return df
