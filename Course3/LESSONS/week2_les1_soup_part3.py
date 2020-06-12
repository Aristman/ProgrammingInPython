from bs4 import BeautifulSoup
from requests import get

html = get('https://www.mars-lab.ru')
soup = BeautifulSoup(html.text, 'lxml')

print(soup.p.find_next_sibling(class_='odd'))
print(list(soup.p.next_siblings))
print(soup.p.find_next_siblings())
print(soup.find('b', text='bold link'))
print(soup.find_all('p', 'odd'))
print(soup.select('p.text.odd'))
print(soup.select('a > b'))

tag = soup.b
print(tag)
tag.name = 'i'
tag['id'] = 'new_id'
tag.string = 'italic'
print(soup.p)

class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)
