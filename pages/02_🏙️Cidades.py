import streamlit as st

import utils.cidades as cdt


def MakeSidebar(df):
    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect(
        "Selecione os Países que Deseja",
        df.loc[:, "country"].unique().tolist(),
        default=   df.loc[:, "country"].unique().tolist(),
    )
    
    st.sidebar.markdown("-----")
    st.sidebar.markdown("Powered by Fabrício")

    return list(countries)


def Main():
    st.set_page_config(page_title="Cities", page_icon=":cityscape:", layout="wide")

    df = cdt.ReadData()

    countries = MakeSidebar(df)

    st.markdown("# :cityscape: Visão Cidades")

    fig = cdt.TopCities(countries)

    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        fig = cdt.TopRestaurants(countries)

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = cdt.WorstRestaurants(countries)

        st.plotly_chart(fig, use_container_width=True)

    fig = cdt.TopCulinarias(countries)

    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    Main()
