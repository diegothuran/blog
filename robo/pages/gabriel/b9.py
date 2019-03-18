# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 80310
RANK_BRAZIL = 3012
NAME = 'b9.com.br'


def get_urls():
    try:
        urls = [] 
        link = 'https://www.b9.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='c-post-card c-post-card--big')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='c-post-card c-post-card--regular')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in b9')

