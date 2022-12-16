import streamlit as st
import utils.paises as pdt


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
    st.set_page_config(page_title="Countries", page_icon=":earth_americas:", layout="wide")

    df = pdt.ReadData()

    countries = MakeSidebar(df)

    st.markdown("# :earth_americas: Visão Países")

    fig = pdt.RestaurantePorPais(countries)

    st.plotly_chart(fig, use_container_width=True)

    fig = pdt.CidadesPorPais(countries)

    st.plotly_chart(fig, use_container_width=True)

    votes, plate_price = st.columns(2)

    with votes:
        fig = pdt.VotosPaisesMedia(countries)

        st.plotly_chart(fig, use_container_width=True)

    with plate_price:
        fig = pdt.PaisesMediaPrato2(countries)

        st.plotly_chart(fig, use_container_width=True)

    return None


if __name__ == "__main__":
    Main()
