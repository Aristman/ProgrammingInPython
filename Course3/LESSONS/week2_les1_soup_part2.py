from requests import get
from bs4 import BeautifulSoup

html = get('https://www.mars-lab.ru').text
soup = BeautifulSoup(html, 'lxml')
print(type(soup.p))
print(soup.p['class'])
print(soup.head.title)
print([tag.name for tag in soup.p.b.parents])

print(soup.p.b.next.next)

print(soup.p.contents)