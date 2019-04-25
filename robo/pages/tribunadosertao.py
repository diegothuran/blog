# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 1538261
RANK_BRAZIL = 65965
NAME = 'tribunadosertao.com.br'

def get_urls():
    try:
        urls = []
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'http://tribunadosertao.com.br/noticias/'
            else:
                link = 'http://tribunadosertao.com.br/noticias/page/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='post-title')
            for noticia in noticias:
#                 print(noticia.find_all('a', href=True)[0]['href'])
                urls.append(noticia.find_all('a', href=True)[0]['href'])
        
        return urls
    except:
        raise Exception('Exception in tribunadosertao')
