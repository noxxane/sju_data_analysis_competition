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

sns.lineplot(dfl, x="Year", y="value", hue="variable")
plt.show()
