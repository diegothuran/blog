# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 86681
RANK_BRAZIL = 2929
NAME = 'jornalopcao.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.jornalopcao.com.br/'
        req = requests.get(link)
        # noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='home-daily-slider')
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='home-daily-featured-title')
        
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href'] 
            if('opcao-play' in href):
                pass
            else:
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornalopcao')
