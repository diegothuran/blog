# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 2394455
RANK_BRAZIL = 83682 
NAME = 'diariodeaparecida.com.br'

def get_urls():
    try:
        urls = [] 
        home = 'http://www.diariodeaparecida.com.br/home/'
        req = requests.get(home)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='thumb-overlay')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href'] 
            print(href)
        
        links = [
            'http://www.diariodeaparecida.com.br/home/category/cidades/',
            'http://www.diariodeaparecida.com.br/home/category/cultura/',
            'http://www.diariodeaparecida.com.br/home/category/goias-online/',
            'http://www.diariodeaparecida.com.br/home/category/economia/',
            'http://www.diariodeaparecida.com.br/home/category/estado/',
            'http://www.diariodeaparecida.com.br/home/category/mundo/',
            'http://www.diariodeaparecida.com.br/home/category/nacional/',
            'http://www.diariodeaparecida.com.br/home/category/politica/'
            ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='post-details')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href'] 
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in diariodeaparecida')

