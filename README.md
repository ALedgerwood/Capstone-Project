# Capstone-Project

Analysis of USD229 budgets from 2014-2023. PDF files available here https://datacentral.ksde.org/budget.aspx

Process Notes:
Data Extraction and Transformation
I used the Python is VS and the Camelot library to extract tables from the budget at a glance (BAG) pdf files and save the tables as csv files. Each pdf hold three years of budget data.
I combined the three BAG csv files I created into a single file.
Earlier budget files (prior to 2014/2014) used a different format, and camelot would not extract table data from them. I attempted to use Pdfplumber with extract the table data, without success. I decided to simply analyze the last ten years of data which was accessible.
Note that Camelot extracted table data from the first table of each pdf, but I had to use Pdfpumber and select the desired page index in order to extract later tables.
Later tables included the Enrollment data, which I saved as separate csv files and combined using the same above steps.
In the predicitve analysis phase, I combined the enrollment and budget data into a single table/csv file when linear regression using Scikitlearn failed using two csv files.
I added a feature of a calculated field for overall percentage change of all the variables. This highlighted the disparity between a 44 percent increase in expenditures and only a 5 percent increase in enrollment over the same time period.
Exploratory Data Analysis
I visualized the data using line graphs using Matplotlin to spot outliers which brought capital investments to light as an outlier. It also emphasized the decrease in enrollment and food services costs during the pandemic years.
Predicitve Analysis
After failed attempts at ETS and Linear Regression due to the small data set, I combined the csv files to a single table. This made Linear Regression and ARIMA possible. Visualizations of the results were questionable, so I performed a correlation analysis which confirmed that the two variables of enrollment and expendtiure are only somewhat correlated. 



