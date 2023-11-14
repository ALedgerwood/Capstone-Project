#using scikitearn to predict enrollment and expenditures

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('EnrandExp.csv', index_col=0, skiprows=[1])

# Assuming the column headers represent years in the format 'YYYY-YYYY'
enrollment_column = 'Enrollment'
expenditure_column = 'Total Expenditures'

# Transpose the dataframe
data = data.transpose()

# Convert values to numeric
data = data.applymap(lambda x: pd.to_numeric(str(x).replace(',', ''), errors='coerce'))

# Extract the relevant columns
X = data[[expenditure_column]]
y = data[enrollment_column]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred, squared=False))

# Visualize the predicted vs actual values
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.title('Linear Regression - Predicted vs Actual')
plt.xlabel(expenditure_column)
plt.ylabel(enrollment_column)
plt.show()
