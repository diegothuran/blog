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
        links = ['https://www1.folha.uol.com.br/ultimas-noticias/',
                 'https://www1.folha.uol.com.br/opiniao/',
                 'https://www1.folha.uol.com.br/poder/',
                 'https://www1.folha.uol.com.br/mercado/',
                 'https://www1.folha.uol.com.br/mundo/',
                 'https://www1.folha.uol.com.br/cotidiano/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='c-main-headline__wrapper')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='c-headline__wrapper')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='c-headline__media-wrapper')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='c-headline c-headline--opinion')   
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                if('.shtml' in href):
                    urls.append(href)
        return urls
    except:
        raise Exception('Exception in fsp')
            
