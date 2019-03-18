# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 2479
RANK_BRAZIL = 73
NAME = 'estadao.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.estadao.com.br/ultimas',
                'https://politica.estadao.com.br/#ultimas',
                'https://economia.estadao.com.br/#ultimas',
                'https://brasil.estadao.com.br/#ultimas',
                'https://internacional.estadao.com.br/#ultimas'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('section', class_='col-md-6 col-sm-6 col-xs-12 col-margin')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='text-wrapper')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
        return urls
    except:
        raise Exception('Exception in estadao')
