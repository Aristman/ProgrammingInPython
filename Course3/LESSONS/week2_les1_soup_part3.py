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
