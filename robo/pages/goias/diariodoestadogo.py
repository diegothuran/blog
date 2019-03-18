# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 1124360
RANK_BRAZIL = 58131
NAME = 'diariodoestadogo.com.br'

def get_urls():
    try:
        urls = [] 
        for i in range(1, PAGE_LIMIT):
            if(i == 1):
                link = 'https://diariodoestadogo.com.br/ultimas/'
            else:
                link = 'https://diariodoestadogo.com.br/ultimas/page/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='vw-block-grid-item')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                if('author' in href):
                    pass
                else:
#                     print(href)
                    urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in diariodoestadogo')
