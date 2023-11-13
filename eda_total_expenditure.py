# exploratory analysis of BAG
#line plot of total expenditures

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('cleaned_BAG_229_2014to2023.csv')

# Assuming "Total Expenditures" is the row header
total_expenditures_row = df.loc[df['Category'] == 'Total Expenditures*']

# Extract the data for plotting
years = df.columns[1:]  # Assuming the years start from the second column

# Convert school years to a range of integers
year_range = [int(year.split('-')[0]) for year in years]

# Define a scaling factor for y-axis (e.g., $1,000,000 for 1 million dollars)
scaling_factor = 1_000_000

# Extract the expenditures from the "Total Expenditures" row and remove commas
expenditures = total_expenditures_row.iloc[:, 1:].values.flatten()
expenditures = [int(expenditure.replace(',', '')) for expenditure in expenditures]

# Transform the expenditures to dollars using integer division
expenditures_in_dollars = [expenditure // scaling_factor for expenditure in expenditures]

# Create a line plot of total expenditures over the school years
plt.plot(year_range, expenditures_in_dollars, marker='o')
plt.title('Total Expenditures Over the School Years 2014 to 2023')
plt.xlabel('School Year')
plt.ylabel('Total Expenditures (Millions of Dollars)')  # Adjust the y-axis label
plt.grid(True)

# Customize the y-axis ticks to begin at 250 and end at 500
y_min = 250
y_max = 450
y_interval = 50  # Set your desired interval
plt.yticks(range(y_min, y_max + y_interval, y_interval))

plt.show()
