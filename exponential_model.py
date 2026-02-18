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
    modeled_values = list(
        map(
            lambda x: round(float(x)), generate_modeled_data(curve_fit, values_to_model)
        )
    )

    real_values += [None, None]

    data = pd.DataFrame(
        {"Year": [1, 2, 3, 4, 5], "Real": real_values, "Modeled": modeled_values}
    )

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
        ry_df = df.loc[df["ry"] == ry]
        ry_df_michigan = ry_df.loc[df["state"] == "MI"]
        ry_sum_michigan = ry_df_michigan["prjtrx"].sum()
        real_values_michigan.append(ry_sum_michigan)
        ry_dict_michigan[ry] = ry_sum_michigan

        ry_df_ohio = ry_df.loc[df["state"] == "OH"]
        ry_sum_ohio = ry_df_ohio["prjtrx"].sum()
        real_values_ohio.append(ry_sum_ohio)
        ry_dict_ohio[ry] = ry_sum_ohio

    year_dict_michigan = {
        1: ry_dict_michigan[3],
        2: ry_dict_michigan[2],
        3: ry_dict_michigan[1],
    }

    real_values_michigan = [
        year_dict_michigan[1],
        year_dict_michigan[2],
        year_dict_michigan[3],
    ]

    year_dict_ohio = {
        1: ry_dict_ohio[3],
        2: ry_dict_ohio[2],
        3: ry_dict_ohio[1],
    }

    real_values_ohio = [
        year_dict_ohio[1],
        year_dict_ohio[2],
        year_dict_ohio[3],
    ]

    x = [1, 2, 3]
    y_michigan = real_values_michigan
    y_ohio = real_values_ohio

    curve_fit_michigan = get_curve_fit(x, y_michigan)
    curve_fit_ohio = get_curve_fit(x, y_ohio)

    values_to_model = [1, 2, 3, 4, 5]
    modeled_values_michigan = list(
        map(
            lambda x: round(float(x)),
            generate_modeled_data(curve_fit_michigan, values_to_model),
        )
    )
    modeled_values_ohio = list(
        map(
            lambda x: round(float(x)),
            generate_modeled_data(curve_fit_ohio, values_to_model),
        )
    )

    real_values_michigan += [None, None]
    real_values_ohio += [None, None]

    data_michigan = pd.DataFrame(
        {
            "Year": [1, 2, 3, 4, 5],
            "Real": real_values_michigan,
            "Modeled": modeled_values_michigan,
        }
    )
    data_ohio = pd.DataFrame(
        {
            "Year": [1, 2, 3, 4, 5],
            "Real": real_values_ohio,
            "Modeled": modeled_values_ohio,
        }
    )

    dfl_michigan = pd.melt(data_michigan, ["Year"])
    dfl_ohio = pd.melt(data_ohio, ["Year"])

    print(dfl_michigan)
    print(dfl_ohio)

    dfl_michigan.to_csv("modeled_data_michigan.csv", index=False)
    dfl_ohio.to_csv("modeled_data_ohio.csv", index=False)


overall_model()
state_models()
