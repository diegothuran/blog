# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 8767
RANK_BRAZIL = 246
NAME = 'ebc.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'http://www.ebc.com.br'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='cmpGeneric isoGrid-item col-lg-4 col-md-4 col-sm-12 col-xs-12')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in ebc')
    