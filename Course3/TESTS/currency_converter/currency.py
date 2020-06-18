from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    def get_value(cur, field):
        return Decimal('1.0000') if cur == 'RUR' \
            else Decimal(soup.find('CharCode', text=cur).find_next_sibling(field).string.replace(',', '.'))

    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp', {'date_req': date})  # Использовать переданный requests
    # ...
    soup = BeautifulSoup(response.content, 'xml')
    cur_from_cours = get_value(cur_from, 'Value')
    cur_from_count = get_value(cur_from, 'Nominal')
    cur_to_cours = get_value(cur_to, 'Value')
    cur_to_count = get_value(cur_to, 'Nominal')
    result = Decimal((amount * cur_from_cours * cur_to_count) / (cur_to_cours * cur_from_count))
    result = result.quantize(Decimal('1.0000'))
    return result  # не забыть про округление до 4х знаков после запятой