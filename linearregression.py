#attempted linear regression to predict expenditures based on enrollment 
#results show the dataset is too small for this and other models see error: 
#ValueError: With n_samples=0, test_size=0.2 and train_size=None, the resulting train set will be empty. Adjust any of the aforementioned parameters.
#even when parameters are adjusted the error remains

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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

# Create new feature: budget per student
merged_data['budget_per_student'] = merged_data['budget'] / merged_data['enrollment']

# Train-test split
X = merged_data[['enrollment', 'budget', 'budget_per_student']]
y = merged_data['expenditures']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choose a model (e.g., Linear Regression)
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Predict expenditures for new data
# Assuming new_data is a DataFrame with columns 'enrollment', 'budget', 'budget_per_student'
new_data['budget_per_student'] = new_data['budget'] / new_data['enrollment']
new_expenditure_predictions = model.predict(new_data[['enrollment', 'budget', 'budget_per_student']])
