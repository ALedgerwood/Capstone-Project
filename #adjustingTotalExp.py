#adjusting Total Expenditures for inflation

import pandas as pd

# Load the CSV file into a DataFrame
file_path = "enrandexp.csv" 
df = pd.read_csv(file_path)

# Extract the Total Expenditures row
total_expenditures_row = df[df['Category'] == 'Total Expenditures'].iloc[:, 1:]

# Convert the expenditure values to integers
total_expenditures_row = total_expenditures_row.apply(lambda x: x.str.replace(',', '').astype(int))

# Choose an inflation index (let's assume CPI) and collect the corresponding data
# You may need to find the actual inflation data for each year
cpi_data = {
    2014:   234.8,
    2015:   236.5,
    2016:   241.4,
    2017:   246.5,
    2018:   251.2,
    2019:   256.9,
    2020:   260.4,
    2021:   278.8,
    2022:   296.7,
    2023:   307.6,
}

# Calculate the inflation rate for each year
inflation_rates = total_expenditures_row.columns.to_series().astype(int).diff().divide(total_expenditures_row.iloc[0, :-1].values).values * 100

# Adjust the expenditures for inflation
adjusted_expenditures = total_expenditures_row.apply(lambda x: x / (1 + inflation_rates / 100))

# Add the adjusted values to the DataFrame
df.loc[df['Category'] == 'Total Expenditures', df.columns[1:]] = adjusted_expenditures.values.flatten()

# Save the adjusted DataFrame to a new CSV file or update the existing one
adjusted_file_path = "adjusted_expenditures.csv"  # Replace with the desired file path
df.to_csv(adjusted_file_path, index=False)

# Print or return the adjusted DataFrame
print(df)
