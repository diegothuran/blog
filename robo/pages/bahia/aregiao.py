# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 613539
RANK_BRAZIL = 34151 
NAME = 'aregiao.com.br'


def get_urls():
    try:
        urls = [] 
        root = 'http://www.aregiao.com.br/'
        # link = 'http://www.aregiao.com.br/'
        req = requests.get(root)
        
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='article-left')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            full_link = root + href 
#             print(full_link)
            urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in aregiao')

