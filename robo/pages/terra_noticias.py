# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 2129
RANK_BRAZIL = 49  
NAME = 'terra.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
            'https://www.terra.com.br/noticias',
            'https://www.terra.com.br/noticias/brasil/',
            'https://www.terra.com.br/noticias/brasil/politica/'
            ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href'] 
    #             print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in terra_noticias')
