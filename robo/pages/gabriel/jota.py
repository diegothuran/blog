# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 62708
RANK_BRAZIL = 2177
NAME = 'jota.info'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.jota.info/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='j-features__title')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h2', class_='j-recent__title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jota')
    