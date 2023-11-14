#scatterplot of correlation of enrollment and expenditures
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the single CSV file
data = pd.read_csv('EnrandExp.csv', index_col=0, skiprows=[1])

# Assuming the column headers represent years in the format 'YYYY-YYYY'
enrollment_column = 'Enrollment'
expenditure_column = 'Total Expenditures'

# Transpose the dataframe
data = data.transpose()

# Convert values to numeric
data = data.applymap(lambda x: pd.to_numeric(str(x).replace(',', ''), errors='coerce'))

# Extract the 'Enrollment' and 'Total Expenditures' columns
enrollment_values = data[enrollment_column]
expenditure_values = data[expenditure_column]

# Create a scatter plot
plt.scatter(enrollment_values, expenditure_values, alpha=0.7)
plt.title(f'Scatter Plot of {enrollment_column} vs {expenditure_column}')
plt.xlabel(enrollment_column)
plt.ylabel(expenditure_column)
plt.grid(True)
plt.show()
