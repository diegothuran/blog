# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 852172
RANK_BRAZIL = 28987
NAME = 'abert.org.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://www.abert.org.br'
        link = 'https://www.abert.org.br/web/index.php/notmenu'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h1')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            full_link = root + href
#             print(href)
            urls.append(full_link)
        return urls
    except:
        raise Exception('Exception in abert')

# print(get_urls())

