# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 6333452
RANK_BRAZIL = None
NAME = 'jornalregional.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'http://www.jornalregional.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='box-800')
        print(noticias)
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornalregional')
