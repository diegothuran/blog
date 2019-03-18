# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 72367
RANK_BRAZIL = 2400
NAME = 'opopular.com.br'


def get_urls():
    try:
        urls = [] 
        links = [
            'https://www.opopular.com.br/editorias/politica',
            'https://www.opopular.com.br/editorias/economia',
            'https://www.opopular.com.br/editorias/mundo',
            'https://www.opopular.com.br/editorias/cidades'
            ]
        
        root = 'https://www.opopular.com.br'
        for link in links:
            req = requests.get(link)
        #     noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='col-md-12 col-sm-6')
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='tag--politica news__side-tag news__text text-content-color')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='news__side-tag news__text text-content-color')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='news__list-text text text-content-color')
            
        #     print(noticias)
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[1]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in opopular')
