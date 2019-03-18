# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 364899
RANK_BRAZIL = 16280 
NAME = 'oestadoce.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.oestadoce.com.br/geral',
                'http://www.oestadoce.com.br/ceara',
                'http://www.oestadoce.com.br/politica',
                'http://www.oestadoce.com.br/economia',
                'http://www.oestadoce.com.br/nacional',
                'http://www.oestadoce.com.br/mundo'                
            ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='nivel-um small-12 columns')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('article', class_='nivel-dois small-12 columns')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('article', class_='nivel-tres small-12 columns')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='article-colunistas col-xs-12')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in oestadoce')

