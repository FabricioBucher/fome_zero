import streamlit as st

import utils.culinaria as cdt


def MakeSidebar(df):
    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect(
        "Selecione os Países que Deseja",
        df.loc[:, "country"].unique().tolist(),
        default=df.loc[:, "country"].unique().tolist(),
    )

    top_n = st.sidebar.slider(
        "Selecione a quantidade de Restaurantes", 1, 30, 15
    )

    cuisines = st.sidebar.multiselect(
        "Escolha os Tipos de Culinária ",
        df.loc[:, "cuisines"].unique().tolist(),
        default=df.loc[:, "cuisines"].unique().tolist()[0:30],
    )
    
    st.sidebar.markdown("-----")
    st.sidebar.markdown("Powered by Fabrício")

    return list(countries), top_n, list(cuisines)


def Main():
    st.set_page_config(page_title="Cuisines", page_icon=":knife_fork_plate:", layout="wide")

    df = cdt.ReadData()

    countries, top_n, cuisines = MakeSidebar(df)

    st.markdown("# :knife_fork_plate: Visão Tipos de Cusinhas")

    df_restaurants = cdt.TopRestaurants(countries, cuisines, top_n)

    st.markdown(f"## Melhores Restaurantes por tipos de Culinária")

    cdt.Metrics()

    st.markdown(f"## Top {top_n} Restaurantes")

    st.dataframe(df_restaurants)

    col1, col2 = st.columns(2)

    with col1:
        fig = cdt.BestCuisines(countries, top_n)

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = cdt.WorstCuisines(countries, top_n)

        st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    Main()
