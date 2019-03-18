# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 451305
RANK_BRAZIL = 18149
NAME = 'jornalivre.com'

def get_urls():
    try:
        urls = [] 
        link = 'https://jornalivre.com/category/noticia/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h1', class_='entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornalivre')
    
