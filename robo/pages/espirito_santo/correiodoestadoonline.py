# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages import PAGE_LIMIT

GLOBAL_RANK = 7484295
RANK_BRAZIL = None
NAME = 'correiodoestadoonline.com.br'


def get_urls():
    try:
        urls = [] 
        for i in range(1, PAGE_LIMIT):
            link = 'http://www.correiodoestadoonline.com.br/noticias/todas/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='col-xs-12 col-sm-12 col-md-12 col-lg-12 li-anuncio')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in correiodoestadoonline')
