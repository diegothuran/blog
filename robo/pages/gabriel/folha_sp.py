# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1167
RANK_BRAZIL = 26
NAME = 'folha.uol.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://www1.folha.uol.com.br/ultimas-noticias/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='flex-cell')
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='c-headline__wrapper')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in folha')
    