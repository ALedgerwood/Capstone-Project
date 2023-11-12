#line plot of Capital Improvements
#indicates Capital Improvements in 2019 was an outlier

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('cleaned_BAG_229_2014to2023.csv')

# Assuming "Capital Improvements" is the row header
capital_improvements_row = df.loc[df['Category'] == 'Capital Improvements']

# Extract the data for plotting
years = df.columns[1:]  # Assuming the years start from the second column

# Convert school years to a range of integers
year_range = [int(year.split('-')[0]) for year in years]

# Define a scaling factor for y-axis (e.g., $1,000,000 for 1 million dollars)
scaling_factor = 1_000_000

# Extract the expenditures from the "Capital Improvements" row and remove commas
capital_improvements = capital_improvements_row.iloc[:, 1:].values.flatten()
capital_improvements = [int(capital_improvements.replace(',', '')) for capital_improvements in capital_improvements]

# Transform the expenditures to dollars using integer division
capital_improvements_in_dollars = [expenditure // scaling_factor for expenditure in capital_improvements]

# Create a line plot of total expenditures over the school years
plt.plot(year_range, capital_improvements_in_dollars, marker='o')
plt.title('Capital Improvements Over the School Years 2014 to 2023')
plt.xlabel('School Year')
plt.ylabel('Capital Improvements (Millions of Dollars)') 
plt.grid(True)

# Customize the y-axis ticks to begin at 0 and end at 35
y_min = 0
y_max = 35
y_interval = 5  # Set your desired interval
plt.yticks(range(y_min, y_max + y_interval, y_interval))

plt.show()