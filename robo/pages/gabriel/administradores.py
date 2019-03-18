# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 11283
RANK_BRAZIL = 666  
NAME = 'administradores.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://www.administradores.com.br'
        link = 'http://www.administradores.com.br/noticias/'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='link')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            full_link = root + href
#             print(href)
            urls.append(full_link)
        return urls
    except:
        raise Exception('Exception in administradores')

# print(get_urls())
