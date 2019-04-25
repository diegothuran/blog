# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 36684
RANK_BRAZIL = 1142
NAME = 'tnh1.com.br'

def get_urls():
    try:
        urls = [] 
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'https://www.tnh1.com.br/noticias/ultimas/'
            else:
                link = 'https://www.tnh1.com.br/noticias/ultimas/pagina/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='noticias-listagem__lista__item__image')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in tnh1')
