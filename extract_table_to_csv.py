import pdfplumber
import pandas as pd

# Define the PDF file path and page number containing the table
pdf_file = "BAG-229-2017.pdf"
page_number = 9  # Change this to the page number you want to extract the table from

# Open the PDF file
with pdfplumber.open(pdf_file) as pdf:
    # Select the page
    page = pdf.pages[page_number - 1]  # Page numbers are 0-based

    # Extract the table from the page
    table = page.extract_table()

# Convert the table data to a Pandas DataFrame
df = pd.DataFrame(table)

# Define the CSV file path where you want to save the data
csv_file = "BAG-229-2017-enrollment.csv"

# Save the extracted table as a CSV file
df.to_csv(csv_file, index=False)

print(f"Data from page {page_number} saved as {csv_file}")







