# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 67372
RANK_BRAZIL = 2344
NAME = 'tribunadoceara.uol.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'http://tribunadoceara.uol.com.br/noticias/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='card__latest--thumb')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in tribunadoceara')

