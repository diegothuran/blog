# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 6082688
RANK_BRAZIL = None
NAME = 'aquiamapa.com.br'


def get_urls():
    try:
        urls = [] 
        link = 'https://aquiamapa.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find('div', class_='footer-widget widget_recent_entries')
        
        list_href = noticias.find_all('a', href=True)
        for i in range(len(list_href)):
#             print(list_href[i]['href'])
            urls.append(list_href[i]['href'])
        
        return urls
    except:
        raise Exception('Exception in aquiamapa')
