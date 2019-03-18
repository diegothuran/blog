import sys

sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 102 
RANK_BRAZIL =  None
NAME = 'bbc.com'


def get_urls():
    try:
        urls = [] 
        link  = 'https://www.bbc.com/portuguese/topics/75612fa6-147c-4a43-97fa-fcf70d9cced3'
        req = requests.get(link)
        itens = BeautifulSoup(req.text, "html.parser").find('div', class_='eagle').find_all('a', class_='title-link')         
        for item in itens:
            href = 'https://www.bbc.com' + item.get('href')
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in bbc')
    