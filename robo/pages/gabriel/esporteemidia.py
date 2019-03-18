# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 171807
RANK_BRAZIL = 6506 
NAME = 'esporteemidia.com'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.esporteemidia.com/'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='post-title entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             full_link = root + href
#             print(href)
            urls.append(href)
        return urls
    except:
        raise Exception('Exception in esporteemidia')

# print(get_urls())

