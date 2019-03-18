# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 13027
RANK_BRAZIL = 301  
NAME = 'camara.leg.br'

def get_urls():
    try:
        urls = [] 
        link = 'http://www2.camara.leg.br/camaranoticias/'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='informacoes')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             full_link = root + href
#             print(href)
            urls.append(href)
        return urls
    except:
        raise Exception('Exception in camara')

# print(get_urls())

