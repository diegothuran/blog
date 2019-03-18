# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 168390
RANK_BRAZIL = 4966
NAME = 'operamundi.uol.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://operamundi.uol.com.br/'
        req = requests.get(link)
        bs = BeautifulSoup(req.text, "html.parser")
        noticias = bs.find('div', class_='news-grid').find_all('a', href=True)
        noticias += bs.find('div', class_='col-xs-12 col-md-6 home-grid').find_all('a', href=True)
        noticias += bs.find('div', class_='col-xs-12 news-grid').find_all('a', href=True)
        noticias += bs.find('div', class_='row news-grid').find_all('a', href=True)
        for noticia in noticias:
            href = noticia['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in operamundi')
    