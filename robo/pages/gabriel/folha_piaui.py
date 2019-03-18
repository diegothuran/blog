# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1167
RANK_BRAZIL = 26 
NAME = 'piaui.folha.uol.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'http://piaui.folha.uol.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='main-content')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='bloco size-1 destaque ')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='bloco size-2 ')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='inner')
        
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in piaui_folha')

