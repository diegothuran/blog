# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 164080
RANK_BRAZIL = 6078
NAME = 'outraspalavras.net'

def get_urls():
    try:
        urls = [] 
        link = 'http://outraspalavras.net/'
        req = requests.get(link)
        
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='featured-entry')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h3', class_='entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in outraspalavras')
    
