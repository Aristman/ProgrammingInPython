from bs4 import BeautifulSoup, NavigableString
import os
import re


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


def get_page_links(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        links = re.findall(r"(?<=/wiki/)[\w()]+", f.read())
    return links


def get_path_recursive(path, start_page, end_page):
    list_files = set(os.listdir(path))
    with open(os.path.join(path, start_page), 'r', encoding='utf-8') as f:
        start_page_links = set(re.findall(r"(?<=/wiki/)[\w()]+", f.read())) & list_files
    if end_page in start_page_links:
        return [start_page]
    for page in start_page_links:
        pass


def build_bridge(path, start_page, end_page):
    """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
    end_page, начальная и конечная страницы включаются в результирующий список"""
    if start_page == end_page:
        return [start_page]
    pages_link_sets = dict()
    list_files = set(os.listdir(path))
    for page in list_files:
        with open(os.path.join(path, page), 'r', encoding='utf-8') as f:
            pages_link_sets[page] = [p for p in set(re.findall(r"(?<=/wiki/)[\w()]+", f.read())) & list_files]
            if page in pages_link_sets[page]:
                pages_link_sets[page].remove(page)
    link_chain = [[start_page]]
    while True:
        new_link_chain = []
        for page in link_chain:
            for new_page in pages_link_sets[page[-1]]:
                new_link_chain.append(page + [new_page])
                if new_page == end_page:
                    return new_link_chain[-1]
        link_chain = new_link_chain


def get_statistics(path, start_page, end_page):
    """собирает статистику со страниц, возвращает словарь, где ключ - название страницы,
    значение - список со статистикой страницы"""

    # получаем список страниц, с которых необходимо собрать статистику
    pages = build_bridge(path, start_page, end_page)
    # напишите вашу реализацию логики по сбору статистики здесь
    statistic = {}
    for page in pages:
        statistic[page] = parse(os.path.join(path, page))
    return statistic
