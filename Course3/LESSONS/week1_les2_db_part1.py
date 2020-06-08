from requests import get
import re

nbrb_html = get('http://nbrb.by')
match = re.search(r'USD 1 Доллар США\D+(\d+,\d+)', nbrb_html.text)
print(f'Курс доллара на сегодня - {match.group(1)}')
print(nbrb_html.text)
