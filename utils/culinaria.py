import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def ReadData():
    return pd.read_csv("./dataset/processed/data.csv")


def TopCuisines():
    df = ReadData()

    cuisines = {
        "Italian": "",
        "American": "",
        "Arabian": "",
        "Japanese": "",
        "Brazilian": "",
    }

    cols = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "cuisines",
        "average_cost_for_two",
        "currency",
        "aggregate_rating",
        "votes",
    ]

    for key in cuisines.keys():

        lines = df["cuisines"] == key

        cuisines[key] = (
            df.loc[lines, cols]
            .sort_values(["aggregate_rating", "restaurant_id"], ascending=[False, True])
            .iloc[0, :]
            .to_dict()
        )

    return cuisines


def Metrics():

    cuisines = TopCuisines()

    italian, american, arabian, japonese, brazilian = st.columns(len(cuisines))

    with italian:
        st.metric(
            label=f'Italiana: {cuisines["Italian"]["restaurant_name"]}',
            value=f'{cuisines["Italian"]["aggregate_rating"]}/5',
            help=f"""
            País: {cuisines["Italian"]['country']}\n
            Cidade: {cuisines["Italian"]['city']}\n
            Média Prato para dois: {cuisines["Italian"]['average_cost_for_two']} - {cuisines["Italian"]['currency']}
            """,
        )

    with american:
        st.metric(
            label=f'Americana: {cuisines["American"]["restaurant_name"]}',
            value=f'{cuisines["American"]["aggregate_rating"]}/5',
            help=f"""
            País: {cuisines["American"]['country']}\n
            Cidade: {cuisines["American"]['city']}\n
            Média Prato para dois: {cuisines["American"]['average_cost_for_two']} - {cuisines["American"]['currency']}
            """,
        )

    with arabian:
        st.metric(
            label=f'Árabe: {cuisines["Arabian"]["restaurant_name"]}',
            value=f'{cuisines["Arabian"]["aggregate_rating"]}/5',
            help=f"""
            País: {cuisines["Arabian"]['country']}\n
            Cidade: {cuisines["Arabian"]['city']}\n
            Média Prato para dois: {cuisines["Arabian"]['average_cost_for_two']} - {cuisines["Arabian"]['currency']}
            """,
        )

    with japonese:
        st.metric(
            label=f'Japonesa: {cuisines["Japanese"]["restaurant_name"]}',
            value=f'{cuisines["Japanese"]["aggregate_rating"]}/5',
            help=f"""
            País: {cuisines["Japanese"]['country']}\n
            Cidade: {cuisines["Japanese"]['city']}\n
            Média Prato para dois: {cuisines["Japanese"]['average_cost_for_two']} - {cuisines["Japanese"]['currency']}
            """,
        )

    with brazilian:
        st.metric(
            label=f'Brasileira: {cuisines["Brazilian"]["restaurant_name"]}',
            value=f'{cuisines["Brazilian"]["aggregate_rating"]}/5',
            help=f"""
            País: {cuisines["Brazilian"]['country']}\n
            Cidade: {cuisines["Brazilian"]['city']}\n
            Média Prato para dois: {cuisines["Brazilian"]['average_cost_for_two']} - {cuisines["Brazilian"]['currency']}
            """,
        )

    return None


def TopRestaurants(countries, cuisines, top_n):
    df = ReadData()

    cols = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "cuisines",
        "average_cost_for_two",
        "aggregate_rating",
        "votes",
    ]

    lines = (df["cuisines"].isin(cuisines)) & (df["country"].isin(countries))

    dataframe = df.loc[lines, cols].sort_values(
        ["aggregate_rating", "restaurant_id"], ascending=[False, True]
    )

    return dataframe.head(top_n)


def BestCuisines(countries, top_n):
    df = ReadData()

    lines = df["country"].isin(countries)

    grouped_df = (
        df.loc[lines, ["aggregate_rating", "cuisines"]]
        .groupby("cuisines")
        .mean()
        .sort_values("aggregate_rating", ascending=False)
        .reset_index()
        .head(top_n)
    )

    fig = px.bar(
        grouped_df.head(top_n),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title=f"{top_n} Melhores Tipos de Culinárias",
        labels={
            "cuisines": "Tipo de Culinária",
            "aggregate_rating": "Média da Avaliação",
        },
    )

    return fig


def WorstCuisines(countries, top_n):
    df = ReadData()

    lines = df["country"].isin(countries)

    grouped_df = (
        df.loc[lines, ["aggregate_rating", "cuisines"]]
        .groupby("cuisines")
        .mean()
        .sort_values("aggregate_rating")
        .reset_index()
        .head(top_n)
    )

    fig = px.bar(
        grouped_df.head(top_n),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title=f"{top_n} Piores Tipos de Culinárias",
        labels={
            "cuisines": "Tipo de Culinária",
            "aggregate_rating": "Média da Avaliação",
        },
    )

    return fig
