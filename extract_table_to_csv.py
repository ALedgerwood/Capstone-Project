import pdfplumber
import pandas as pd

# Replace 'input.pdf' with the path to your PDF file.
pdf_file = "BAG-229-2014.pdf"

# Specify the page number (e.g., page 3) to extract data from.
page_number = 3

# Define bounding boxes for text extraction (adjust coordinates as needed).
# The bounding box should encompass the area where the table is located.
bbox = [50, 100, 550, 500]  # Example coordinates

# Use pdfplumber to open the PDF file and extract text
with pdfplumber.open(pdf_file) as pdf:
    page = pdf.pages[page_number - 1]  # Page numbers are 0-based

    # Extract text from the specified bounding box
    table_text = page.within_bbox(bbox).extract_text()

# Split the extracted text into lines
lines = table_text.split('\n')

# Extract headers and data
headers = lines[0].split()  # Assuming headers are in the first line

# Extract data rows, accounting for varying row lengths
data_rows = [line.split() for line in lines[1:] if line.strip()]

# Create a DataFrame
df = pd.DataFrame(data_rows, columns=headers)

# Save the DataFrame as a CSV file
df.to_csv("BAG-229-2014_page3.csv", index=False)





