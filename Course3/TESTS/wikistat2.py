from bs4 import BeautifulSoup, NavigableString
from wikistat1 import parse
import os
import re


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
                new_link_chain.append(page+[new_page])
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


