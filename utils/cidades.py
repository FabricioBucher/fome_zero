import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def ReadData():
    return pd.read_csv("./dataset/processed/data.csv")


def TopCities(countries):
    df = ReadData()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["restaurant_id", "country", "city"]]
        .groupby(["country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(10),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=",.2f",
        color="country",
        title="Top 10 Cidades com mais Restaurantes",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de Restaurantes",
            "country": "País",
        },
    )

    return fig


def TopRestaurants(countries):
    df = ReadData()

    grouped_df = (
        df.loc[
            (df["aggregate_rating"] >= 4) & (df["country"].isin(countries)),
            ["restaurant_id", "country", "city"],
        ]
        .groupby(["country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(10),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=",.2f",
        color="country",
        title="Top 10 Cidades com Restaurantes com média acima de 4",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de Restaurantes",
            "country": "País",
        },
    )

    return fig


def WorstRestaurants(countries):
    df = ReadData()

    grouped_df = (
        df.loc[
            (df["aggregate_rating"] <= 2.5) & (df["country"].isin(countries)),
            ["restaurant_id", "country", "city"],
        ]
        .groupby(["country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(10),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=",.2f",
        color="country",
        title="Piores 10 Cidades com Restaurantes com média abaixo de 2.5",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de Restaurantes",
            "country": "País",
        },
    )

    return fig


def TopCulinarias(countries):
    df = ReadData()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["cuisines", "country", "city"]]
        .groupby(["country", "city"])
        .nunique()
        .sort_values(["cuisines", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(10),
        x="city",
        y="cuisines",
        text="cuisines",
        color="country",
        title="Top 10 Cidades com mais restaurantes com tipos culinários distintos",
        labels={
            "city": "Cidades",
            "cuisines": "Quantidade de Tipos Culinários Únicos",
            "country": "País",
        },
    )

    return fig
