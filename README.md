# Capstone-Project

Analysis of USD229 budgets from 2014-2023. PDF files available here https://datacentral.ksde.org/budget.aspx

Process Notes:
I used the Python is VS and the Camelot library to extract tables from the budget at a glance (BAG) pdf files and save the tables as csv files. Each pdf hold three years of budget data.
I combined the three BAG csv files I created into a single file.
Earlier budget files (prior to 2014/2014) used a different format, and camelot would not extract table data from them. I attempted to use Pdfplumber with extract the table data, without success. I decided to simply analyze the last ten years of data which was accessible.
Note that Camelot extracted table data from the first table of each pdf, but I had to use Pdfpumber and select the desired page index in order to extract later tables.
Later tables included the Enrollment data, which I saved as separate csv files and combined using the same above steps.
