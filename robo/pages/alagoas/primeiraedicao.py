# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 3201961
RANK_BRAZIL = None
NAME = 'primeiraedicao.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://primeiraedicao.com.br'
        for i in range(1, PAGE_LIMIT):
            if(i == 1):
                link = 'http://primeiraedicao.com.br/noticias'
            else:
                link = 'http://primeiraedicao.com.br/noticias?page=' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='envolve_conteudo_lista')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in primemiraedicao')
