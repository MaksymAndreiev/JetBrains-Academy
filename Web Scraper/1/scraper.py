import requests

web_site = input('Input the URL:')
req = requests.get(web_site)
if req.status_code == 200 and 'content' in req.json().keys():
    print(req.json()['content'])
else:
    print('Invalid quote resource!')
