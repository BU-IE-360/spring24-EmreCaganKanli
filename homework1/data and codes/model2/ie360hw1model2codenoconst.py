import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_percentage_error
import matplotlib.pyplot as plt

# Read data
all_data = pd.read_excel("all data.xlsx")

# Separate features and target
X = all_data.drop(columns=["Date", "konut"])
t = all_data["t"]
y = pd.DataFrame(all_data["konut"])

# Set train and test data
y_train = y.iloc[:].copy()
y_test = y.iloc[:].copy()
X_train = X.iloc[:].copy()
X_test = X.iloc[:].copy()
t_train = t.iloc[:].copy()
t_test = t.iloc[:].copy()

# linear model
model = sm.OLS(y_train, X_train)
results = model.fit()
print(results.summary())

# Forecast 
forecast = results.predict(X_test)
forecast = pd.DataFrame(forecast)
model_residuals = y_test.values - forecast.values

# Plot residuals
plt.plot(model_residuals, label='Residual Analysis')
plt.legend()
plt.show()

# Calculate MAPE
mape = mean_absolute_percentage_error(y_test, forecast)
print("MAPE of the model:", mape)

# Plot actual vs forecast for both cases
plt.plot(y.index, y, label='Actual')
plt.plot(y.index, forecast, label='Forecast')
plt.legend()
plt.show()
