#Compiling data from five csv files into a single file

import pandas as pd

# List of CSV file paths you want to combine
csv_files = ['BAG-229-2017-enrollment.csv', 'BAG-229-2020-enrollment.csv', 'BAG-229-2023-enrollment.csv']

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through the list of CSV files and read each one into a DataFrame
for file in csv_files:
    data = pd.read_csv(file)
    combined_data = pd.concat([combined_data, data], ignore_index=True)

# Save the combined data to a new CSV file
combined_data.to_csv('combined_BAG_229_enrollment.csv', index=False)
