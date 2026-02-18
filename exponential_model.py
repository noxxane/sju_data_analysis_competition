import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def get_curve_fit(x_data, y_data):
    coeffs = np.polyfit(x_data, np.log(y_data), 1)

    def exponential_func(x):
        return np.exp(coeffs[1]) * np.exp(coeffs[0] * x)
    
    return exponential_func

def generate_modeled_data(curve_fit, x_values):
    return [curve_fit(x) for x in x_values]

def overall_model():
    df = pd.read_csv("Team_02_-_Camden_Catholic_A.csv")
    real_values = []
    ry_dict = {}

    for ry in [3, 2, 1]:
        ry_df = df.loc[df["ry"] == ry]
        ry_sum = ry_df["prjtrx"].sum()
        real_values.append(ry_sum)
        ry_dict[ry] = ry_sum

    year_dict = {1: ry_dict[3], 2: ry_dict[2], 3: ry_dict[1]}
    real_values = [year_dict[1], year_dict[2], year_dict[3]]

    x = [1, 2, 3]
    y = real_values

    curve_fit = get_curve_fit(x, y)

    values_to_model = [1, 2, 3, 4, 5]
    modeled_values = list(map(lambda x: round(float(x)), generate_modeled_data(curve_fit, values_to_model)))

    real_values += [None, None]

    data = pd.DataFrame({
        "Year": [1, 2, 3, 4, 5],
        "Real": real_values,
        "Modeled": modeled_values})

    dfl = pd.melt(data, ["Year"])
    print(dfl)

    dfl.to_csv("modeled_data.csv", index=False)

def state_models():
    df = pd.read_csv("Team_02_-_Camden_Catholic_A.csv")
    real_values_michigan = []
    real_values_ohio = []
    ry_dict_michigan = {}
    ry_dict_ohio = {}

    for ry in [3, 2, 1]:
        ry_df_michigan = df.loc[(df["ry"] == ry) and (df["state"] == "MI")]
        ry_sum_michigan = ry_df["prjtrx"].sum()
        real_values_michigan.append(ry_sum_michigan)
        ry_dict_michigan[ry] = ry_sum_michigan

        ry_df_ohio = df.loc[(df["ry"] == ry) and (df["state"] == "OH")]
        ry_sum_ohio = ry_df["prjtrx"].sum()
        real_values_ohio.append(ry_sum_ohio)
        ry_dict_ohio[ry] = ry_sum_ohio

    year_dict_michigan = {1: ry_dict_michigan[3], 2: ry_dict_michigan[2], 1: ry_dict_michigan[1]}
    real_values_michigan = [year_dict_michigan[1], year_dict_michigan[2], year_dict_michigan[3]]

    year_dict_ohio = {1: ry_dict_ohio[3], 2: ry_dict_ohio[2], 1: ry_dict_ohio[1]}
    real_values_ohio = [year_dict_ohio[1], year_dict_ohio[2], year_dict_ohio[3]]

    x = [1, 2, 3]
    y_michigan = real_values_michigan
