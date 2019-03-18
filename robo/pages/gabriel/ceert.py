# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 490914
RANK_BRAZIL = 19676 
NAME = 'ceert.org.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.ceert.org.br/noticias'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-sm-12 col-md-6')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-sm-8')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             full_link = root + href
#             print(href)
            urls.append(href)
        return urls
    except:
        raise Exception('Exception in ceert')

# print(get_urls())


