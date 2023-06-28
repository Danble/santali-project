
from pdfminer import high_level
from pdfminer.layout import LAParams

# Specify the path to your PDF file
pdf_path = 'example.pdf'

# Specify the path for the output HTML file
output_html_path = 'output.html'

# Extract text from PDF and save as HTML
with open(output_html_path, 'wb') as output_file, open(pdf_path, 'rb') as input_file:
    high_level.extract_text_to_fp(input_file, output_file, laparams=LAParams(), output_type='html')