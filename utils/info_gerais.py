import pandas as pd

def QtdRestaurants(dataframe):
    return dataframe.shape[0]


def QtdCountries(dataframe):
    return dataframe.loc[:, "country"].nunique()


def QtdCities(dataframe):
    return dataframe.loc[:, "city"].nunique()


def QtdRatings(dataframe):
    return dataframe.loc[:, "votes"].sum()


def QtdCuisines(dataframe):
    return dataframe.loc[:, "cuisines"].nunique()
