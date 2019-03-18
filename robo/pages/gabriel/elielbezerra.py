# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = None
RANK_BRAZIL = None
NAME = 'elielbezerra.blogspot.com'

def get_urls():
    try:
        urls = [] 
        link = 'http://elielbezerra.blogspot.com/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='post-title entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in elielbezerra')
    