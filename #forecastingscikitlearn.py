#forecasting and visualization using Arima
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load your data and transpose it
data = pd.read_csv('EnrandExp.csv', index_col=0).transpose()

# Extract the relevant rows
enrollment_row = 'Enrollment'
expenditure_row = 'Total Expenditures'

# Remove commas from 'Enrollment' row and convert to numeric
data[enrollment_row] = data[enrollment_row].apply(lambda x: pd.to_numeric(str(x).replace(',', ''), errors='coerce'))

# Remove commas from 'Total Expenditures' row and convert to numeric
data[expenditure_row] = data[expenditure_row].apply(lambda x: pd.to_numeric(str(x).replace(',', ''), errors='coerce'))

# Convert the year column to datetime format
data.index = pd.to_datetime(data.index, format='%Y')

# Extract the time series for expenditures
time_series = data[expenditure_row].astype(float)  # Ensure data is numeric

# Define ARIMA order
order = (1, 1, 1)  # Example order, you might need to tune this

# Train ARIMA model
model = ARIMA(time_series, order=order)
results = model.fit()

# Forecast future values
future_steps = 3
forecast = results.get_forecast(steps=future_steps).predicted_mean

# Generate future dates for the forecast
future_dates = pd.date_range(start=data.index[-1], periods=future_steps + 1, freq='Y')[1:]

# Visualize historical data and predictions
plt.plot(time_series.index, time_series.values, label='Historical Expenditures')
plt.plot(future_dates, forecast, color='red', linestyle='dashed', label='Predicted Expenditures')

plt.title('Historical Data and Predictions - Expenditures Over Years')
plt.xlabel('Year')
plt.ylabel('Expenditures')
plt.legend()
plt.show()

