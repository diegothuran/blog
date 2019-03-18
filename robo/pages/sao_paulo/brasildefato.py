# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 55267
RANK_BRAZIL = 2058   
NAME = 'brasildefato.com.br'


def get_urls():
    try:
        root = 'https://www.brasildefato.com.br'
        urls = [] 
        links = [
                'https://www.brasildefato.com.br/ultimas_noticias/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='news-item-link divisor')
#             noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='text-wrapper')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
#                 print(full_link)
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in brasildefato')

# get_urls()