# converts HTML files to PDF files using wkhtmltopdf tool.
# this script was created with assistance from ChatGPT
# note wkhtmltopdf is not maintained consistently and you should look for another solution
import os
import subprocess

# Specify the directory containing HTML files
html_dir = 'kb/original'

# Specify the output directory for PDF files
pdf_dir = 'kb/pdf'

# Make sure the output directory exists
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

# List all HTML files in the directory
html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]

for html_file in html_files:
    # Build the input and output file paths
    input_path = os.path.join(html_dir, html_file)
    output_file = os.path.splitext(html_file)[0] + '.pdf'
    output_path = os.path.join(pdf_dir, output_file)

    # Convert HTML to PDF using wkhtmltopdf
    cmd = ['wkhtmltopdf', input_path, output_path]
    subprocess.run(cmd)

    print(f'Converted {html_file} to {output_file}')

print("Conversion complete.")
