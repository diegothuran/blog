# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = None
RANK_BRAZIL = None
NAME = 'blogdoluciosorge.com.br'


def get_urls():
    try:
        urls = [] 
        link = 'http://www.blogdoluciosorge.com.br/category/politica/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='common-category-entry-title')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h2', class_='destaque-menor left')
        
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in blogdoluciosorge')
    
