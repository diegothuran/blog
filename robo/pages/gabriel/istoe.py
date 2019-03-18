# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 10240
RANK_BRAZIL = 225
NAME = 'istoe.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://istoe.com.br/ultimas/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='wrapper-title no-image')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='wrapper-image')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='row')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in istoe')
    
