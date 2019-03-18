# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 4444 
RANK_BRAZIL = 129  
NAME = 'dc.clicrbs.com.br'

def get_urls():
    try:
        urls = []
        link = 'http://dc.clicrbs.com.br/sc/noticias/ultimas-noticias/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='title')
        for noticia in noticias:
            try:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
            except: 
                pass
        return urls
    except:
        raise Exception('Exception in diariocatarinense')
