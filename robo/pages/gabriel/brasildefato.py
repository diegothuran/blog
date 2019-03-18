# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 56469
RANK_BRAZIL = 1596
NAME = 'brasildefato.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://www.brasildefato.com.br'
        link = 'https://www.brasildefato.com.br/ultimas_noticias/'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='news-item-link divisor')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            full_link = root + href
#             print(href)
            urls.append(full_link)
        return urls
    except:
        raise Exception('Exception in brasildefato')

# print(get_urls())

