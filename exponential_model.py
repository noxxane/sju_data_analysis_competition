import numpy as np

def get_curve_fit(x_data, y_data):
    coeffs = np.polyfit(np.exp(x), y, 1)
    return np.poly1d(coeffs)

def generate_modeled_data(curve_fit, x_values):
    return [curve_fit(x) for x in x_values]

x = np.array([1, 2, 3])
y = np.array([4, 9, 16])

curve_fit = get_curve_fit(x, y)

values_to_model = [1, 2, 3, 4, 5]
print(generate_modeled_data(curve_fit, values_to_model))
