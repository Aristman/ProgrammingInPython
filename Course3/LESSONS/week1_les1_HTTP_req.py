from requests import get, post, codes
import json

page = get('http://google.com')
print(page.status_code)
print(page.headers)
req = post('http://google.com')
print('-------')
print(req.text)
print('----------------------------------\n'*3)
page = get('http://github.com')
print(page.url)
print(page.status_code)
print(page.history)
page = get('http://github.com', allow_redirects=False)
print(page.status_code)
print(page.url)
print('=========================\n'*3)
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
page = get(url, cookies=cookies)
print(page.text)