# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 13914
RANK_BRAZIL = 408 
NAME = 'correiobraziliense.com.br'


def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.correiobraziliense.com.br/politica/',
                'https://www.correiobraziliense.com.br/cidades---df/',
                'https://www.correiobraziliense.com.br/brasil/',
                'https://www.correiobraziliense.com.br/economia/',
                'https://www.correiobraziliense.com.br/mundo/'
            ]
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-md-6 mb-16')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('h4', class_='txt-serif mt-0 mb-10')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href'] 
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in correiobraziliense')
