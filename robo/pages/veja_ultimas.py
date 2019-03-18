# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 936 
RANK_BRAZIL = 25  
NAME = 'veja.abril.com.br'


def get_urls():
    try:
        urls = [] 
        
        link = 'https://veja.abril.com.br/ultimas-noticias/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='list-item')
        for noticia in noticias:
#             print(noticia.find_all('a', href=True)[0]['href'])
            urls.append(noticia.find_all('a', href=True)[0]['href'])
        
        return urls
    except:
        raise Exception('Exception in veja_ultimas')
