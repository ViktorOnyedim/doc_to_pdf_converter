import os
import pypandoc
from sys import argv


def convert_doc_to_pdf(doc_path):
    # Check if the file exists
    if not os.path.exists(doc_path):
        raise ValueError("The file does not exist")

    # Define the output PDF path
    pdf_path = os.path.splitext(doc_path)[0] + '.pdf'

    try:
        # Convert DOC/DOCX to PDF
        pypandoc.convert_file(doc_path, 'pdf', outputfile=pdf_path)
        print(f"Conversion successful! PDF saved at: {pdf_path}")
    except Exception as e:
        print(f"Conversion failed. Error: {e}")

if __name__ == "__main__":
    doc_path = str(argv[1])
    convert_doc_to_pdf(doc_path)
