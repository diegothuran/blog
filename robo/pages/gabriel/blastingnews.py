# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1355
RANK_BRAZIL = None
NAME = 'br.blastingnews.com'


def get_urls():
    try:
        urls = [] 
        link = 'https://br.blastingnews.com/brasil/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='title-news')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h3', class_='title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in blastingnews')

