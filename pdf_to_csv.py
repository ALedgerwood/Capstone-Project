###Convert table data in a pdf file to csv file
import camelot

# Replace 'input.pdf' with the path to your PDF file.
pdf_file = "BAG-229-2017.pdf"

# Use camelot to extract the table data from the PDF.
tables = camelot.read_pdf(pdf_file, flavor='lattice', pages='1-end')

# Replace 'output.csv' with the desired CSV file name.
tables[0].to_csv("BAG-229-2017.csv")
