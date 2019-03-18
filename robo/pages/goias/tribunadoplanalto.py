# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 1177159
RANK_BRAZIL = 71292
NAME = 'tribunadoplanalto.com.br'

def get_urls():
    try:
        urls = [] 
        for i in range(1, PAGE_LIMIT):
            if(i == 1):
                link = 'http://tribunadoplanalto.com.br/ultimas-noticias/'
            else:
                link = 'http://tribunadoplanalto.com.br/ultimas-noticias/page/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='td-module-thumb')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in tribunadoplanalto')