# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 2248591
RANK_BRAZIL = 72241
NAME = 'noticiaagora.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.noticiaagora.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='modulo')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in noticiaagora')
