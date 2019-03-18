# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1616009
RANK_BRAZIL = None
NAME = 'oquartopoder.com'


def get_urls():
    try:
        urls = [] 
        link = 'https://www.oquartopoder.com/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='titulo-carrosel')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            print(href)
        
        links = [
                'https://www.oquartopoder.com/policia/',
                'https://www.oquartopoder.com/geral/',
                'https://www.oquartopoder.com/politica/',
                'https://www.oquartopoder.com/celebridades/'
            ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='destaque-thumb')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in oquartopoder')
