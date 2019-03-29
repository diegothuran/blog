# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages import PAGE_LIMIT

GLOBAL_RANK = 20035
RANK_BRAZIL = 584  
NAME = 'diariodonordeste.verdesmares.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://diariodonordeste.verdesmares.com.br/'
        for i in range(1, PAGE_LIMIT):
            link = 'http://diariodonordeste.verdesmares.com.br/servicos/ultima-hora?page=' + str(i) +'#pagination'
            
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='c-teaser__text')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in diariodonordeste')
