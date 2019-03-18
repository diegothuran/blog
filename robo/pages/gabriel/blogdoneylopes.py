# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 6059387
RANK_BRAZIL = None
NAME = 'blogdoneylopes.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://blogdoneylopes.com.br'
        link = 'http://blogdoneylopes.com.br/'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='grid-item')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            full_link = root + href
#             print(href)
            urls.append(full_link)
        return urls
    except:
        raise Exception('Exception in blogdoneylopes')

# print(get_urls())

