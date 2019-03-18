# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 118359
RANK_BRAZIL = 3062 
NAME = 'cartamaior.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.cartamaior.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='titulo_box_1 col-md-12')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in cartamaior')
    
    