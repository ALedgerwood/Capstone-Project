# exploratory analysis of BAG
#line plot of total expenditures

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('cleaned_BAG_229_2014to2023.csv')

# Assuming "Total Expenditures" is the row header
total_expenditures_row = df.loc[df['Category'] == 'Total Expenditures*']

# Extract the data for plotting
years = df.columns[1:]  # Assuming the years start from the second column
expenditures = total_expenditures_row.iloc[:, 1:].values.flatten()

# Convert school years to a range of integers
year_range = [int(year.split('-')[0]) for year in years]

# Define a scaling factor for y-axis (e.g., $1,000,000 for 1 million dollars)
scaling_factor = 1_000_000

# Transform the expenditures to dollars using the scaling factor
expenditures_in_dollars = [expenditure / scaling_factor for expenditure in expenditures]

# Create a line plot of total expenditures over the school years
plt.plot(year_range, expenditures_in_dollars, marker='o')
plt.title('Total Expenditures Over the School Years')
plt.xlabel('School Year')
plt.ylabel('Total Expenditures (Millions of Dollars)')  # Adjust the y-axis label
plt.grid(True)

# Customize the y-axis ticks
plt.yticks(np.arange(250, 350, 50))  # Set y-axis ticks at 250, 300, etc.

plt.show()
