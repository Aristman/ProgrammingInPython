from requests import get
import re
from bs4 import BeautifulSoup
request = get('https://wikipedia.org')
html = request.text
result = re.findall(r'<a[^>]*other-project-link[^>]*href="([^"]*)', html)
print(result)

soup = BeautifulSoup(html, 'lxml')
tags = [tag['href'] for tag in soup('a', 'other-project-link')]
print(tags)
