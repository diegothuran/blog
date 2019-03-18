# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 232107
RANK_BRAZIL = 7464 
NAME = 'tribunaonline.com.br'


def get_urls():
    try:
        urls = [] 
        root = 'https://tribunaonline.com.br'
        links = [
                'https://tribunaonline.com.br/categoria/cidades',
                'https://tribunaonline.com.br/categoria/economia',
                'https://tribunaonline.com.br/categoria/policia',
                'https://tribunaonline.com.br/categoria/politica',
                'https://tribunaonline.com.br/categoria/internacional'
            ]
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-sm-8')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in tribunaonline')
