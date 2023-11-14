#correlation calculations using pandas
#The result is Correlation between Enrollment and Total Expenditures: 0.6871470884757843
#This is a moderate positive correlation

import pandas as pd

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

# Calculate the correlation
correlation = enrollment_values.corr(expenditure_values)

# Print the correlation coefficient
print(f'Correlation between {enrollment_column} and {expenditure_column}: {correlation}')

