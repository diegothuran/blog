# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 30215
RANK_BRAZIL = 1061
NAME = 'migalhas.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.migalhas.com.br/Quentes'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='tituloQuente')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in migalhas')
    
