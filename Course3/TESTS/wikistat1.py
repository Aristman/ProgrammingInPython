from bs4 import BeautifulSoup, NavigableString
import unittest


def find_tag_list(tag_list, tag_name):
    result = 0
    for tag_ol in tag_list.find_all(tag_name):
        if tag_ol.find_parents(('ul', 'ol')) == []:
            result += 1
    return result


def find_a_recursive(soup):
    max_count_a = 0
    count_a = 0
    isSquence = False
    for tag in soup.contents:
        if tag.name == 'a' and isSquence:
            count_a += 1
        elif tag.name == 'a' and not isSquence:
            count_a = 1
            isSquence = True
        elif isinstance(tag, NavigableString):
            continue
        else:
            isSquence = False
            if count_a > max_count_a:
                max_count_a = count_a
    for child_tag in soup.children:
        if not isinstance(child_tag, NavigableString):
            count_a = find_a_recursive(child_tag)
        if count_a > max_count_a:
            max_count_a = count_a
    return max_count_a


def parse(path_to_file):
    imgs = headers = linkslen = lists = 0
    with open(path_to_file, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    source_soup = soup.find('div', id='bodyContent')
    for img in source_soup.find_all('img', width=True):
        if int(img.get('width')) > 199:
            imgs += 1

    for h in source_soup.find_all(('h1', 'h2', 'h3', 'h4', 'h5', 'h6')):
        if h.text[0] in ['E', 'T', 'C']:
            headers += 1

    linkslen = find_a_recursive(source_soup)

    lists += find_tag_list(source_soup, ('ul', 'ol'))
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
    unittest.main()
