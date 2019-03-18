# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1134994
RANK_BRAZIL = None
NAME = 'blogdoataide.com.br'


def get_urls():
    try:
        urls = [] 
        link = 'http://www.blogdoataide.com.br/categoria/politica/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='post-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in blogdoataide')

