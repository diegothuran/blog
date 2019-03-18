# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 818727
RANK_BRAZIL = 25829
NAME = 'blogmarcosfrahm.com'


def get_urls():
    try:
        urls = [] 
        link = 'http://blogmarcosfrahm.com/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h5', class_='titulo-destaque')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h2', class_='entry-title')

        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in blogmarcosfrahm')
    
