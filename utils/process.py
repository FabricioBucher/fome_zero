import inflection
import pandas as pd

COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}


COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}


def RenameColumns(df):
    cols = []
    for i in df.columns:
        cols.append(i.replace(' ', '_').lower().lstrip().rstrip())
    df.columns= cols

    return df


def CountryName(country_id):
    return COUNTRIES[country_id]


def ColorName(color_code):
    return COLORS[color_code]


def CreatePriceTye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"


def ColumnsOrder(df):
    df = df.copy()

    new_cols_order = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "address",
        "locality",
        "locality_verbose",
        "longitude",
        "latitude",
        "cuisines",
        "price_type",
        "average_cost_for_two",
        "currency",
        "has_table_booking",
        "has_online_delivery",
        "is_delivering_now",
        "aggregate_rating",
        "rating_color",
        "color_name",
        "rating_text",
        "votes",
    ]

    return df.loc[:, new_cols_order]


def PrepareData(path):
    df = pd.read_csv(path)

    df = RenameColumns(df)

    df = df.dropna()
    
    df = df.drop_duplicates()

    df["price_type"] = df.loc[:, "price_range"].apply(lambda x: CreatePriceTye(x))

    df["country"] = df.loc[:, "country_code"].apply(lambda x: CountryName(x))

    df["color_name"] = df.loc[:, "rating_color"].apply(lambda x: ColorName(x))

    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])


    df = ColumnsOrder(df)

    df.to_csv("dataset/processed/data.csv", index=False)

    return df
