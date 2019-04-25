# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 17110
RANK_BRAZIL = 548 
NAME = 'ne10.uol.com.br'


def get_urls():
    try:
        urls = [] 
        for i in range(1,PAGE_LIMIT):
            link = 'https://ne10.uol.com.br/radar/buscar/page:' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='listagemDeNoticia-item')
            for noticia in noticias:
#                 print(noticia.find_all('a', href=True)[0]['href'])
                urls.append(noticia.find_all('a', href=True)[0]['href'])
        
        return urls
    except:
        raise Exception('Exception in ne10')

