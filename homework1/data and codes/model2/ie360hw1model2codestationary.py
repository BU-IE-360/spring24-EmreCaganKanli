import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

# Read data
all_data = pd.read_excel("all data.xlsx")

# Separate features and target
t = all_data["t"]
y = all_data["konut"]

# Check stationary
print("Initial p-value for stationary test: " + str(adfuller(y)[1]))

# Plot acf and pacf plots
plot_acf(y)
plt.show()

plot_pacf(y)
plt.show()
