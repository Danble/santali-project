from bs4 import BeautifulSoup

# Read the HTML file
with open('output.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Define the filtering function
def filter_span(tag):
    if tag.name == 'span' and tag.has_attr('style') and 'font-family: CMBXTI10' in tag['style']:
        return True
    return False

filtered_spans = soup.find_all(filter_span)

with open('output.txt', 'w') as file:
    for span in filtered_spans:
        file.write(span.get_text() + '\n')
