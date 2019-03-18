# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 8767
RANK_BRAZIL = 246
NAME = 'agenciabrasil.ebc.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'http://agenciabrasil.ebc.com.br/ultimas'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='isoGrid-item')
        for noticia in noticias:
            href = 'http://agenciabrasil.ebc.com.br' + noticia.find('h3', class_= 'heading').find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in agenciabrasil')
    