import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def ReadData():
    return pd.read_csv("./dataset/processed/data.csv")


def RestaurantePorPais(countries):
    df = ReadData()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["restaurant_id", "country"]]
        .groupby("country")
        .count()
        .sort_values("restaurant_id", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="restaurant_id",
        text="restaurant_id",
        title="Quantidade de Restaurantes por País",
        labels={
            "country": "Paises",
            "restaurant_id": "Quantidade de Restaurantes",
        },
    )

    return fig


def CidadesPorPais(countries):
    df = ReadData()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["city", "country"]]
        .groupby("country")
        .nunique()
        .sort_values("city", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="city",
        text="city",
        title="Quantidade de Cidades por País",
        labels={
            "country": "Paises",
            "city": "Quantidade de Cidades",
        },
    )

    return fig


def VotosPaisesMedia(countries):
    df = ReadData()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["votes", "country"]]
        .groupby("country")
        .mean()
        .sort_values("votes", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="votes",
        text="votes",
        text_auto=",.2f",
        title="Média de Avaliações por País",
        labels={
            "country": "Paises",
            "votes": "Quantidade de Avaliações",
        },
    )

    return fig


def PaisesMediaPrato2(countries):
    df = ReadData()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["average_cost_for_two", "country"]]
        .groupby("country")
        .mean()
        .sort_values("average_cost_for_two", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="average_cost_for_two",
        text="average_cost_for_two",
        text_auto=",.2f",
        title="Média de Preço de prato para 2 por País",
        labels={
            "country": "Paises",
            "average_cost_for_two": "Preço de prato para 2",
        },
    )

    return fig
