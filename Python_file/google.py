from invoice2data import extract_data
from invoice2data.extract.loader import read_templates

template = read_templates('Template/')

result = extract_data('Invoice/google.pdf', templates=template)


for i in result:
    print(i, ' :', result[i])
