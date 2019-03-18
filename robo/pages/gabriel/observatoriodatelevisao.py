# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

#pegou o indice de bol.uol.com.br
GLOBAL_RANK = 938 
RANK_BRAZIL = 27  
NAME = 'observatoriodatelevisao.bol.uol.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://observatoriodatelevisao.bol.uol.com.br/noticias-da-tv'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='entry-title td-module-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in observatoriodatelevisao')
    

