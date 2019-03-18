# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1706585
RANK_BRAZIL = 74945  
NAME = 'istoenoticia.com'

def get_urls():
    try:
        urls = [] 
        link = 'http://istoenoticia.com/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='feature-title')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h4', class_='entry-title')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h3', class_='entry-title')
        
        
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in istoenoticia')
