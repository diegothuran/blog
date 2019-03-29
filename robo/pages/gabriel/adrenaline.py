# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests
from robo.pages import PAGE_LIMIT

GLOBAL_RANK = 12313
RANK_BRAZIL = 394  
NAME = 'adrenaline.uol.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https:'
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'https://adrenaline.uol.com.br/arquivo/tipo=noticia/'
            else:
                link = 'https://adrenaline.uol.com.br/arquivo/tipo=noticia/pagina/' + str(i)
        
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='full-width')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
#                 print(href)
                urls.append(full_link)
        return urls
    except:
        raise Exception('Exception in adrenaline')

# print(get_urls())

