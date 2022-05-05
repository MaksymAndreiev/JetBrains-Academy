import requests
import json
from bs4 import BeautifulSoup

web_site = input('Input the URL: ')
if 'title' not in web_site:
    print('Invalid movie page!')
else:
    r = requests.get(web_site, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        if soup.find('title').text != '' and soup.find('meta', {'name': 'description'})['content']:
            dict_ = {'title': soup.find('h1').text, 'description': soup.find('span', {'class': 'GenresAndPlot__TextContainerBreakpointXL-sc-cum89p-2 eqbKRZ'}).text}
            print(dict_)
        else:
            print('Invalid movie page!')
    else:
        print('Invalid movie page!')
