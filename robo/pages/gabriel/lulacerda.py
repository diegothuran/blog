# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

# pegou o rank do ig
GLOBAL_RANK = 2707
RANK_BRAZIL = 64  
NAME = 'lulacerda.ig.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://lulacerda.ig.com.br/'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2')
        for noticia in noticias:
            try:
                href = noticia.find_all('a', href=True)[0]['href']
    #             full_link = root + href
    #             print(href)
                urls.append(href)
            except:
                pass
        return urls
    except:
        raise Exception('Exception in lulacerda')

# print(get_urls())


