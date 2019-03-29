# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages import PAGE_LIMIT

GLOBAL_RANK = 99261
RANK_BRAZIL = 3836 
NAME = 'istoedinheiro.com.br'

def get_urls():
    try:
        urls = [] 
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'https://www.istoedinheiro.com.br/ultimas/'
            else:
                link = 'https://www.istoedinheiro.com.br/ultimas/page/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3')
            try:
                for noticia in noticias:
#                     print(noticia.find_all('a', href=True)[0]['href'])
                    urls.append(noticia.find_all('a', href=True)[0]['href'])
            except: # alguns h3 nao tem o link
                pass
        
        return urls
    except:
        raise Exception('Exception in istoedinheiro')
