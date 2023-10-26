# python code to convert html files in one directory into pdf files
# this was generated with the help of ChatGPT
import os
import pdfkit

# Specify the directory containing HTML files
html_dir = 'path/to/your/html/files/directory'

# Specify the output directory for PDF files
pdf_dir = 'path/to/output/pdf/files/directory'

# List all HTML files in the directory
html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]

# Make sure the output directory exists
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

# Initialize pdfkit options
options = {
    'quiet': '',
}

for html_file in html_files:
    # Build the input and output file paths
    input_path = os.path.join(html_dir, html_file)
    output_file = os.path.splitext(html_file)[0] + '.pdf'
    output_path = os.path.join(pdf_dir, output_file)

    # Convert HTML to PDF
    pdfkit.from_file(input_path, output_path, options=options)
    print(f'Converted {html_file} to {output_file}')

print("Conversion complete.")