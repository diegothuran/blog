# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 188076
RANK_BRAZIL = 7717 
NAME = 'mundodomarketing.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.mundodomarketing.com.br/ultimas-noticias'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='camadaLink2')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h2', class_='titulodestaque')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in mundodomarketing')
    
