import PyPDF2
import pdfplumber
import pyperclip
import subprocess
import os
import io
from fpdf import FPDF

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Function to copy text to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)

# Function to run Fabric summarization and other patterns
def run_fabric_patterns():
    try:
        print("Running Fabric pattern: summarize")
        result = subprocess.run(
            ["fabric", "--pattern", "summarize"],
            input=pyperclip.paste(),
            text=True,
            capture_output=True
        )
        print(result.stdout)
        print(result.stderr)

        print("Running Fabric pattern: create_report_finding")
        result = subprocess.run(
            ["fabric", "--pattern", "create_report_finding"],
            input=pyperclip.paste(),
            text=True,
            capture_output=True
        )
        print(result.stdout)
        print(result.stderr)

        print("Running Fabric pattern: extract_references")
        result = subprocess.run(
            ["fabric", "--pattern", "extract_references"],
            input=pyperclip.paste(),
            text=True,
            capture_output=True
        )
        print(result.stdout)
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running Fabric pattern: {e}")
    except subprocess.TimeoutExpired:
        print("Process timed out")
    except KeyboardInterrupt:
        print("Process interrupted by user")

# Function to read summary from clipboard (assuming Fabric copies the result to clipboard)
def read_summary_from_clipboard():
    return pyperclip.paste()

# Function to create a new PDF with the summary text
class UTF8FPDF(FPDF):
    def _putpages(self):
        nb = self.page
        if nb == 0:
            return
        # Add _putpages method to handle UTF-8 encoding properly
        for n in range(1, nb + 1):
            self.pages[n] = self.pages[n].encode("latin1", "replace").decode("latin1")
        super()._putpages()

def create_summary_pdf(summary_text):
    pdf = UTF8FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in summary_text.split('\n'):
        pdf.multi_cell(0, 10, txt=line, border=0, align='L', fill=False)
    return pdf

# Combine summary PDF with original PDF
def combine_pdfs(summary_pdf, original_pdf_path, output_pdf_path):
    with open(original_pdf_path, 'rb') as original_file:
        original_pdf = PyPDF2.PdfReader(original_file)
        writer = PyPDF2.PdfWriter()

        # Add summary pages first
        summary_pdf_output = summary_pdf.output(dest='S').encode('latin1')
        summary_reader = PyPDF2.PdfReader(io.BytesIO(summary_pdf_output))
        for page_num in range(len(summary_reader.pages)):
            writer.add_page(summary_reader.pages[page_num])

        # Add original pages
        for page_num in range(len(original_pdf.pages)):
            writer.add_page(original_pdf.pages[page_num])

        # Write to the output PDF
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

# Main function to process PDFs
def process_pdfs(pdf_folder_path):
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder_path, filename)
            print(f"Processing PDF: {pdf_path}")
            text = extract_text_from_pdf(pdf_path)
            copy_to_clipboard(text)
            run_fabric_patterns()
            summary_text = read_summary_from_clipboard()
            summary_pdf = create_summary_pdf(summary_text)
            new_filename = "summarized_" + filename  # Example new filename
            output_pdf_path = os.path.join(pdf_folder_path, new_filename)
            combine_pdfs(summary_pdf, pdf_path, output_pdf_path)
            print(f"Created summarized PDF: {output_pdf_path}")

if __name__ == "__main__":
    pdf_folder_path = "./sourcePDFs"  # Adjust the path if necessary
    process_pdfs(pdf_folder_path)