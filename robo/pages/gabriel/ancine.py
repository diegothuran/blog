# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 188435
RANK_BRAZIL = 8864 
NAME = 'ancine.gov.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.ancine.gov.br/pt-br'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='destaque')
#         noticias += BeautifulSoup(req.text, "html.parser").find_all('h3')
        
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             full_link = root + href
            print(href)
            urls.append(href)
        return urls
    except:
        raise Exception('Exception in ancine')

# print(get_urls())



