# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 60197
RANK_BRAZIL = 2149
NAME = 'ocafezinho.com'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.ocafezinho.com/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='highlight text-center')
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='box')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in ocafezinho')
    
