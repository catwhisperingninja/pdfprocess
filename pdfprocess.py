import PyPDF2
import pdfplumber
import pyperclip
import subprocess
import os
import io
from fpdf import FPDF
from tqdm import tqdm
import colorama

# from Claude
def check_write_permissions(pdf_folder_path):
    if os.access(pdf_folder_path, os.W_OK):
        print(f"Have write permission for {pdf_folder_path}")
    else:
        print(f"No write permission for {pdf_folder_path}")

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
    patterns = ["summarize", "create_report_finding", "extract_references"]
    combined_output = ""
    for pattern in patterns:
        try:
            print(f"Running Fabric pattern: {pattern}")
            result = subprocess.run(
                ["fabric", "--pattern", pattern],
                input=pyperclip.paste(),
                text=True,
                capture_output=True,
                timeout=60
            )
            output = result.stdout.strip()
            combined_output += f"CHATGPT SUMMARY CREATED BY https://github.com/danielmiessler/fabric ----- USING **{pattern.upper()}** FABRIC PATTERN\n{output}\n\n"
            print(f"Stdout for {pattern}:\n{output[:500]}...\n")
            print(f"Stderr for {pattern}:\n{result.stderr}\n")
            print(f"Return code for {pattern}: {result.returncode}\n")
        except Exception as e:
            print(f"Error running pattern {pattern}: {str(e)}")
    return combined_output

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
        for n in range(1, nb + 1):  # Changed 'nb + n' to 'nb + 1'
            self.pages[n] = self.pages[n].encode("latin1", "replace").decode("latin1")
        super()._putpages()



def create_summary_pdf(summary_text):
    pdf = UTF8FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", size=14)
    for line in summary_text.split('\n'):
        if line.startswith("CHATGPT SUMMARY CREATED BY"):
            pdf.set_font("Arial", "B", size=14)
        elif line.startswith("**") and line.endswith("**"):
            pdf.set_font("Arial", "B", size=12)
        else:
            pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=line, border=0, align='L', fill=False)
    return pdf


def combine_pdfs(summary_pdf, original_pdf_path, output_pdf_path):
    try:
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
        print(f"Successfully combined PDFs: {output_pdf_path}")
    except Exception as e:
        print(f"Error combining PDFs: {str(e)}")

# Initialize colorama for Windows compatibility
colorama.init()

from tqdm import tqdm
import colorama

# Initialize colorama for Windows compatibility
colorama.init()

# Define color codes (using colorama for better compatibility)
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
RESET = colorama.Fore.RESET

def process_pdfs(pdf_folder_path):
    pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith('.pdf')]
    
    # Overall progress bar in yellow
    for filename in tqdm(pdf_files, desc="Overall Progress", colour='yellow'):
        try:
            pdf_path = os.path.join(pdf_folder_path, filename)
            print(f"\nProcessing PDF: {pdf_path}")
            
            # Individual file progress bar in yellow
            with tqdm(total=5, desc=f"Processing {filename}", leave=False, colour='yellow') as pbar:
                try:
                    text = extract_text_from_pdf(pdf_path)
                    pbar.update(1)
                except Exception as e:
                    print(f"{RED}Error extracting text: {str(e)}{RESET}")
                
                try:
                    copy_to_clipboard(text)
                    pbar.update(1)
                except Exception as e:
                    print(f"{RED}Error copying to clipboard: {str(e)}{RESET}")
                
                try:
                    fabric_output = run_fabric_patterns()
                    pbar.update(1)
                except Exception as e:
                    print(f"{RED}Error running Fabric patterns: {str(e)}{RESET}")
                
                try:
                    summary_pdf = create_summary_pdf(fabric_output)
                    pbar.update(1)
                except Exception as e:
                    print(f"{RED}Error creating summary PDF: {str(e)}{RESET}")
                
                try:
                    new_filename = "summarized_" + filename
                    output_pdf_path = os.path.join(pdf_folder_path, new_filename)
                    combine_pdfs(summary_pdf, pdf_path, output_pdf_path)
                    pbar.update(1)
                except Exception as e:
                    print(f"{RED}Error combining PDFs: {str(e)}{RESET}")
                
            print(f"{GREEN}Created summarized PDF: {output_pdf_path}{RESET}")
        except Exception as e:
            print(f"{RED}Error processing {filename}: {str(e)}{RESET}")

    # Completion progress bar in green
    with tqdm(total=1, desc="Completion", colour='green') as pbar:
        pbar.update(1)
    print(f"{GREEN}All PDFs processed successfully!{RESET}")

if __name__ == "__main__":
    pdf_folder_path = "./sourcePDFs"  # Adjust the path if necessary
    check_write_permissions(pdf_folder_path)
    process_pdfs(pdf_folder_path)