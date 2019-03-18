# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 325206
RANK_BRAZIL = 14750
NAME = 'tribunadainternet.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'http://www.tribunadainternet.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h1', class_='entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in tribunadainternet')
    
