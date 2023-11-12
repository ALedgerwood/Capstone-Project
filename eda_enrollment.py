#line plot of enrollment
#shows the decrease in total enrollment during pandemic years 2020/2021 and 2021/2022

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('cleaned_BAG-229-2020-enrollment.csv')

# Assuming "Enrollment" is the row header
enrollment_row = df.loc[df['Category'] == 'Enrollment (FTE)*']

# Extract the data for plotting
years = df.columns[1:]  # Assuming the years start from the second column

# Convert school years to a range of integers
year_range = [int(year.split('-')[0]) for year in years]

# Extract the expenditures from the "Enrollment" row and remove commas
enrollment = enrollment_row.iloc[:, 1:].values.flatten()
enrollment = [int(enrollment.replace(',', '')) for enrollment in enrollment]

# Create a line plot of total expenditures over the school years
plt.plot(year_range, enrollment, marker='o')
plt.title('Enrollment Over the School Years 2014 to 2023')
plt.xlabel('School Year')
plt.ylabel('Enrollment') 
plt.grid(True)

plt.show()