# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 367032
RANK_BRAZIL = 13412
NAME = 'blogdopaulinho.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://blogdopaulinho.com.br/'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h1', class_='entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             full_link = root + href
#             print(href)
            urls.append(href)
        return urls
    except:
        raise Exception('Exception in blogdopaulinho')

# print(get_urls())

