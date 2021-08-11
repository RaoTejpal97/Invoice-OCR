from invoice2data import extract_data
from invoice2data.extract.loader import read_templates

templates = read_templates('Template/')

result = extract_data('Invoice/oyo.pdf', templates=templates)

x = len(result)
for i in result:
    print(i, ' :', result[i])
