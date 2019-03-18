# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 934 
RANK_BRAZIL = 25  
NAME = 'veja.abril.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://veja.abril.com.br/noticias-sobre/eleicoes-2018/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='content widget-home-box-list')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='highlight-bullets')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in veja_abril')
    