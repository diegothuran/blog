# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 305057
RANK_BRAZIL = 10132 
NAME = 'diariodoamapa.com.br'

def get_urls():
    try:
        urls = [] 
        for i in range(1, PAGE_LIMIT):
            print(' --------' + str(i))
            if(i == 1):
                link = 'https://www.diariodoamapa.com.br/category/cadernos/ultima-hora/'
            else:
                link = 'https://www.diariodoamapa.com.br/category/cadernos/ultima-hora/page/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col col-xs-12 col-sm-9 col-md-9')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in diariodoamapa')
