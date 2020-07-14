import requests
url = "https://datasend.webpython.graders.eldf.ru/submissions/1/"
headers = {'Authorization': 'Basic', 'username': 'alladin', 'password': 'YWxsYWRpbjpvcGVuc2VzYW1l'}

req = requests.Request(method='post',url=url,headers=headers)
print(req)
req.json