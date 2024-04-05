import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

# Read data
all_data = pd.read_excel("all data.xlsx")
all_data["Hafta"] = pd.to_datetime(all_data["Hafta"], format='%d-%m-%Y')

# Separate features and target
bayram = all_data["bayram"]
ramazan = all_data["ramazan"]
kurban = all_data["kurban"]
t = all_data["t"]
y = all_data["Clothing"]


print("Correlation between Bayram Search and Ramazan Search: " + str(bayram.corr(ramazan)))
print("Correlation between Bayram Search and Kurban Search: " + str(bayram.corr(kurban)))
print("Correlation between Ramazan Search and Kurban Search: " + str(ramazan.corr(kurban)))

# Check stationary
print("Initial p-value for stationary test: " + str(adfuller(y)[1]))

# Plot acf and pacf plots
plot_acf(y)
plt.show()

plot_pacf(y)
plt.show()

# Differencing
y_diff = y.diff().dropna()

# Check stationary
print("First Difference p-value for stationary test: " + str(adfuller(y_diff)[1]))

# Plot acf and pacf plots
plot_acf(y_diff)
plt.show()

plot_pacf(y_diff)
plt.show()

plt.plot(y_diff.index, y_diff)
plt.show()


y_diff_log = y.apply(lambda x: np.log(x)).diff().dropna()

plt.plot(y_diff.index, y_diff_log)
plt.show()

# Check stationary
print("First Difference of log transform p-value for stationary test: " + str(adfuller(y_diff_log)[1]))

# Plot acf and pacf plots
plot_acf(y_diff_log)
plt.show()

plot_pacf(y_diff_log)
plt.show()
