# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1089663
RANK_BRAZIL = 34187
NAME = 'ohoje.com.br'


def get_urls():
    try:
        urls = [] 
        root = 'http://www.ohoje.com.br'
        req = requests.get(root)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='pltc')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            full_link = root + href 
#             print(full_link)
            urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in ohoje')
