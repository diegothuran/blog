# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 6765
RANK_BRAZIL = 214
NAME = 'www.eb.mil.br'

def get_urls():
    try:
        urls = []
        link = 'http://www.eb.mil.br/web/noticias/noticiario-do-exercito'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='asset-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            urls.append(href)
        return urls
    except:
        raise Exception('Exception in eb')

# print(get_urls())

