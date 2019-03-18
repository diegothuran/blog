# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 88221
RANK_BRAZIL = 2106
NAME = 'imprensaviva.com'

def get_urls():
    try:
        urls = [] 
        link = 'http://www.imprensaviva.com/search/label/Pol%C3%ADtica'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='post-title entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in imprensaviva')
    