#fetch cpi data from final quarter of each year
import pandas_datareader as pdr
import datetime

# Set the start and end dates for CPI data
start_date = datetime.datetime(2014, 1, 1)
end_date = datetime.datetime(2022, 12, 31)

# Fetch CPI data from FRED
cpi_data = pdr.get_data_fred('CPIAUCNS', start_date, end_date)

# Select the data for the final quarter of each year
cpi_data_final_quarter = cpi_data.groupby(cpi_data.index.year).last()

# Print the obtained CPI data for the final quarter of each year
print(cpi_data_final_quarter)



