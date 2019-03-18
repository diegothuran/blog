# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 28580 
RANK_BRAZIL =  924  
NAME = 'correio24horas.com.br'

def get_urls():
    try:  
        urls = []  
        for i in range(1,PAGE_LIMIT):
            link = 'https://www.correio24horas.com.br/noticias/pagina/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='noticias-listagem--item-meta')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href'] 
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in correioi24horas')