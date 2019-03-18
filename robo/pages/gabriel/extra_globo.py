# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 148 
RANK_BRAZIL = 5
NAME = 'extra.globo.com'

def get_urls():
    try:
        urls = [] 
        link = 'https://extra.globo.com/noticias/plantao.html'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='text')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in extra_globo')
    
