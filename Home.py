import folium
import pandas as pd
import streamlit as st
from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static

from utils import info_gerais as ig
from utils.process import PrepareData

RAW_DATA_PATH = f"./dataset/zomato.csv"


def MakeSidebar(df):
    image_path = "./img/"
    image = Image.open(image_path + "logo.png")

    col1, col2 = st.sidebar.columns([1, 4])
    col1.image(image, width=65)
    col2.markdown("# Fome Zero")

    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect(
        "Selecione os Países que Deseja",
        df.loc[:, "country"].unique().tolist(),
        default=df.loc[:, "country"].unique().tolist()[0:7],
    )
    
    st.sidebar.markdown("-----")
    st.sidebar.markdown("### Download Dados Tratados")

    processed_data = pd.read_csv("./dataset/processed/data.csv")

    st.sidebar.download_button(
        label="Download",
        data=processed_data.to_csv(index=False),
        file_name="data.csv",
        mime="text/csv",
    )
    
    st.sidebar.markdown("-----")
    st.sidebar.markdown("Powered by Fabrício")

    return list(countries)


def CreateMap(dataframe):
    f = folium.Figure(width=1920, height=1080)

    m = folium.Map(
        location=[ dataframe['latitude'].median(), dataframe['longitude'].median() ],
        zoom_start=2,
        max_bounds=True
    ).add_to(f)

    marker_cluster = MarkerCluster().add_to(m)

    for _, line in dataframe.iterrows():

        name = line["restaurant_name"]
        price_for_two = line["average_cost_for_two"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = f'{line["color_name"]}'

        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {},00 ({}) para dois"
        html += "<br />Type: {}"
        html += "<br />Aggragate Rating: {}/5.0"
        html = html.format(name, price_for_two, currency, cuisine, rating)

        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )

        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa"),
        ).add_to(marker_cluster)

    folium_static(m, width=1024, height=768)


def Main():

    df = PrepareData(RAW_DATA_PATH)

    st.set_page_config(page_title="Home", page_icon=":bar_chart:", layout="wide")

    selected_countries = MakeSidebar(df)
    
    st.markdown("# Fome Zero!")

    st.markdown("## O Melhor lugar para encontrar seu mais novo restaurante favorito!")

    st.markdown("### Temos as seguintes marcas dentro da nossa plataforma:")

    restaurants, countries, cities, ratings, cuisines = st.columns(5)

    restaurants.metric(
        "Número de Restaurantes",
        ig.QtdRestaurants(df),
        )
    countries.metric(
        "Número de Países",
        ig.QtdCountries(df),
    )

    cities.metric(
        "Número de Cidades",
        ig.QtdCities(df),
    )

    ratings.metric(
        "Número de Avaliações Feitas",
        f"{ig.QtdRatings(df):,}".replace(",", "."),
    )

    cuisines.metric(
        f"Tipos de Culinárias",
        f"{ig.QtdCuisines(df):,}",
    )

    map_df = df.loc[df["country"].isin(selected_countries), :]

    CreateMap(map_df)

    return None


if __name__ == "__main__":
    Main()
