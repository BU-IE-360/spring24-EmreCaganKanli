import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_percentage_error
import matplotlib.pyplot as plt

# Read data
all_data = pd.read_excel("all data.xlsx")
# Separate features and target
X = all_data.drop(columns=["Date", "eur"])
X = sm.add_constant(X)
t = all_data["t"]
y = pd.DataFrame(all_data["eur"])
y = y.apply(lambda x: np.log(x))

# Set train and test data
y_train = y.iloc[:].copy()
y_test = y.iloc[:].copy()
X_train = X.iloc[:].copy()
X_test = X.iloc[:].copy()
t_train = t.iloc[:].copy()
t_test = t.iloc[:].copy()

# Linear Model
model = sm.OLS(y_train, X_train)
results = model.fit()
print(results.summary())

# Forecast of the model
forecast = results.predict(X_test)
forecast = pd.DataFrame(forecast).apply(lambda x: np.exp(x))
model_residuals = y_test.apply(lambda x: np.exp(x)).values - forecast.values

# Plot residuals
plt.plot(model_residuals, label='Residual Analysis')
plt.legend()
plt.show()

# Calculate MAPE
mape = mean_absolute_percentage_error(y_test.apply(lambda x: np.exp(x)), forecast)
print("MAPE:", mape)

# Plot actual vs forecast for both cases
plt.plot(y.index, y.apply(lambda x: np.exp(x)), label='Actual')
plt.plot(y.index, forecast, label='Forecast')
plt.legend()
plt.show()
