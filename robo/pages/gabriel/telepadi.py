# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

# pegou o indice de folha.uol.com.br
GLOBAL_RANK = 1167
RANK_BRAZIL = 26
NAME = 'telepadi.folha.uol.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://telepadi.folha.uol.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('p', class_='resumo')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h2', class_='titulo')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in telepadi')
    
