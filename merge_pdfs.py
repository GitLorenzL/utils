import PyPDF2
import sys

def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfWriter()
    for path in paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if len(sys.argv) < 3:
    print("Usage: python merge_pdfs.py [pdf1] [pdf2] ...")
    sys.exit(1)

# File paths are taken from command line arguments
pdfs = sys.argv[1:]

# Output file name
output = "merged.pdf"

# Merge the two PDFs
merge_pdfs(pdfs, output)
print("PDFs merged successfully into", output)
