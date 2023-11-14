#ETS for predictive modeling
#does not yet work becuase of a problem with arrays, see error:
#ValueError: Pandas data cast to numpy dtype of object. Check input data with np.asarray(data).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Load data
enrollment_data = pd.read_csv('cleaned_BAG-229-2020-enrollment.csv', skiprows=1)
budget_data = pd.read_csv('cleaned_BAG_229_2014to2023.csv', skiprows=1)

# Melt the data to have 'year' as a separate column
enrollment_melted = enrollment_data.melt(var_name='year', value_name='enrollment')
budget_melted = budget_data.melt(var_name='year', value_name='budget')

# Merge data based on the 'year' column
merged_data = pd.merge(enrollment_melted, budget_melted, on='year')

# Extract the total expenditure as the target variable
# Assuming the total expenditure is in the last column of the budget data
merged_data['expenditures'] = merged_data.iloc[:, -1]

# Prepare data for ETS
ets_data = merged_data[['year', 'expenditures']]
ets_data.columns = ['ds', 'y']
ets_data['ds'] = pd.to_datetime(ets_data['ds'])

# Fit an ETS model
model_ets = ExponentialSmoothing(ets_data['y'], trend='add', seasonal='add', seasonal_periods=1)  # Assuming no seasonality
result_ets = model_ets.fit()

# Make predictions
forecast_ets = result_ets.forecast(steps=10)  # Adjust the number of steps as needed

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(ets_data['ds'], ets_data['y'], label='Actual Expenditures')
plt.plot(pd.date_range(start=ets_data['ds'].max(), periods=10, freq='Y'), forecast_ets, label='ETS Forecast', color='red')
plt.title('Expenditures Forecast with ETS')
plt.xlabel('Year')
plt.ylabel('Expenditures')
plt.legend()
plt.show()
