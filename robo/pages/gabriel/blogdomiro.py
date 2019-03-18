# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 197192
RANK_BRAZIL = 5693
NAME = 'altamiroborges.blogspot.com'


def get_urls():
    try:
        urls = [] 
        link = 'https://altamiroborges.blogspot.com/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='post hentry')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in altamiroborges')

