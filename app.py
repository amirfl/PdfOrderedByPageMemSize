import pypdf
import sys
import os

# create a directory named 'input'
if not os.path.exists('output'):
    os.mkdir('output')

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'input.pdf'

# Open the PDF file in read-binary mode
reader = pypdf.PdfReader(filename)

# Create a list to store the size of each page
page_sizes = []

# Loop through each page of the PDF
for page_num, page in enumerate(reader.pages):
    # Get the memory size of the page
    size = len(page.get_contents().get_data())
    # Add the size to the list
    page_sizes.append((page_num, size))


# Sort the page sizes list by the size of each page
sorted_page_sizes = sorted(page_sizes, key=lambda x: x[1])

print(sorted_page_sizes)

# Create a pypdf PdfWriter object
writer = pypdf.PdfWriter()

# Loop through the pages in the sorted order
for page_num, size in sorted_page_sizes:
    # Get the page from the original PDF and add it to the new PDF
    page = reader.pages[page_num]
    writer.add_page(page)

# Write the new PDF file to disk
with open('output/output.pdf', 'wb') as output_file:
    writer.write(output_file)
