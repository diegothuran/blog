# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 3326177
RANK_BRAZIL = None
NAME = 'blogdoriella.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'http://blogdoriella.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='post-title entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in blogdoriella')
    
