# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 903084
RANK_BRAZIL = 31811
NAME = 'grandesnomesdapropaganda.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://grandesnomesdapropaganda.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='entry-title td-module-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in grandesnomesdapropaganda')

