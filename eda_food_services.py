#line plot of Food Services expenditures
#indicates decrease during pandemic, but overall increase outpacing enrollment increase

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('cleaned_BAG_229_2014to2023.csv')

# Assuming "Food Services" is the row header
food_services_row = df.loc[df['Category'] == 'Food Services']

# Extract the data for plotting
years = df.columns[1:]  # Assuming the years start from the second column

# Convert school years to a range of integers
year_range = [int(year.split('-')[0]) for year in years]

# Define a scaling factor for y-axis (e.g., $1,000,000 for 1 million dollars)
scaling_factor = 1_000_000

# Extract the expenditures from the "Capital Improvements" row and remove commas
food_services = food_services_row.iloc[:, 1:].values.flatten()
food_services = [int(food_services.replace(',', '')) for food_services in food_services]

# Transform the expenditures to dollars using integer division
food_services_in_dollars = [food_services // scaling_factor for food_services in food_services]

# Create a line plot of food services costs over the school years
plt.plot(year_range, food_services_in_dollars, marker='o')
plt.title('Food Services Costs Over the School Years 2014 to 2023')
plt.xlabel('School Year')
plt.ylabel('Food Services Costs (Millions of Dollars)') 
plt.grid(True)

# Customize the y-axis ticks to begin at 5 and end at 15
y_min = 5
y_max = 15
y_interval = 1  # Set your desired interval
plt.yticks(range(y_min, y_max + y_interval, y_interval))

plt.show()