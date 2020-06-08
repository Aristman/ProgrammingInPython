from bs4 import BeautifulSoup
import os
import unittest


def parse(path_to_file):
    # Поместите ваш код здесь.
    # ВАЖНО!!!
    # При открытии файла, добавьте в функцию open необязательный параметр
    # encoding='utf-8', его отсутствие в коде будет вызвать падение вашего
    # решения на грейдере с ошибкой UnicodeDecodeError
    imgs = headers = linkslen = lists = 0
    with open(path_to_file, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    img_soup = soup.find('div', id='bodyContent')
    for img in img_soup.find_all('img', width=True):
        if int(img.get('width')) > 199:
            imgs += 1
    for h in soup.find_all(('h1', 'h2', 'h3', 'h4', 'h5', 'h6'), id=False):
        if h.text[0] in ['E', 'T', 'C']:
            headers +=1
    links_list = soup.find_all('a')


    return [imgs, headers, linkslen, lists]


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


if __name__ == '__main__':
    #unittest.main()
    print(parse('wiki/Stone_Age'))
    print(parse('wiki/Brain'))
    print(parse('wiki/Artificial_intelligence'))
    print(parse('wiki/Python_(programming_language)'))
    print(parse('wiki/Spectrogram'))