# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 9612832
RANK_BRAZIL = None
NAME = 'avozeavezdajuventude.blogspot.com'


def get_urls():
    try:
        urls = [] 
        link = 'http://avozeavezdajuventude.blogspot.com/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='post-outer')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in avozeavezdajuventude')
