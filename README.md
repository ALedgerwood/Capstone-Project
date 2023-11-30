# Capstone-Project

Analysis of USD229 budgets from 2014-2023. PDF files available here https://datacentral.ksde.org/budget.aspx

Overfleaf report can be found here https://www.overleaf.com/read/cqyfrpfzcjzq#80bbd9  

Process Notes:

### Exploration of data sources

I used the Python in VS and the Camelot and PDFplumber libraries to extract tables from the budget at a glance (BAG) PDF files and save the tables as CSV files. Each PDF held three years of budget data.

I combined the three BAG CSV files I created into a single file.

Earlier budget files (prior to 2014/2014) used a different format, and Camelot would not extract table data from them. I attempted to use Pdfplumber with extract the table data, without success. I decided to simply analyze the last ten years of data which was accessible.

Note that Camelot extracted table data from the first table of each pdf, but I had to use Pdfpumber and select the desired page index in order to extract later tables.

Later tables included the Enrollment data, which I saved as separate CSV files and combined using the same above steps.

### Cleaning and wrangling the data

In later Predictive analysis, I realized I could combine the budget CSV file and enrollment CSV file because they covered the same years. Referencing a single file was much easier, and it made the dataset slightly larger for machine leanring test/train splits.

I added the feature of a calculated field to find the percentage of change in each category. This made it clear that spending increases outpaced those in enrollment. It also made outliers quite clear. 

I visualized the data using line graphs using Matplotlib to spot outliers which brought capital investments to light as an outlier. It also emphasized the decrease in enrollment and food services costs during the pandemic years.

### Designing and deploying a predictive model

After failed attempts at ETS and Linear Regression due to the small data set, I combined the csv files to a single table. This made Linear Regression and ARIMA possible. Visualizations showed the results of ML were not very reliable, so I performed a correlation analysis which confirmed that the two variables of enrollment and expenditure are only somewhat correlated. Using Scikitlearn, I was able to visualize a prediction of values for a future three years.

### Conclusions:

The findings revealed a number of unexpected complicating factors which make predictions based one existing data less than reliable. The history of district spending did not experience a steady increase as one might expect in a district with rising enrollment. Rather, there were outliers in several categories including capital investments and food services costs. So past funding might not be the a reliable indicator of future spending needs. Enrollment too reflected unexpected variation, due to the pandemic impacts felt nation-wide.

### Limitations:
Machine learning attempts revealed the data set it too small to make accurate predictions, and the variables of enrollment and attendance are only moderately correlated. Future work suggests adding more variables or additional data is needed to make reliable predictions for future funding.

