# Capstone-Project

Analysis of USD229 budgets from 2014-2023. PDF files available here https://datacentral.ksde.org/budget.aspx

Process Notes:
I used the camelot library to save tables as csv files. Each pdf hold three years of budget data.
I combine the three csv files into a single file.
Earlier budget files used a different format, and camelot would not extract it. I attempted to use pdfplumber with extract the table data, without success. I decided to simply analyze the last ten years of data which was accessible.
