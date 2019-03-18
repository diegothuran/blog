# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 158
RANK_BRAZIL = 9   
NAME = 'noticias.uol.com.br'


def get_urls():
    try:
        urls = [] 
        links = [
            'https://noticias.uol.com.br/politica/',
            'https://noticias.uol.com.br/jornais/',
            'https://noticias.uol.com.br/internacional/',
            'https://noticias.uol.com.br/ultimas',
            'https://economia.uol.com.br/ultimas/'
            ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_=' thumbnail-standard-wrapper')
            for noticia in noticias:
                try:
                    href = noticia.find_all('a', href=True)[0]['href'] 
#                     print(href)
                    urls.append(href)
                except:
                    pass
        return urls
    except:
        raise Exception('Exception in uol')
