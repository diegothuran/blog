# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 3879141
RANK_BRAZIL = None    
NAME = 'cinform.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.cinform.com.br/category/sergipe/',
                'https://www.cinform.com.br/category/nacional/',
                'https://www.cinform.com.br/category/mundo/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='vw-post-box__title')
            
            for noticia in noticias:
                try:
                    href = noticia.find_all('a', href=True)[0]['href']
                    urls.append(href)
                except:
                    pass
        return urls
    except:
        raise Exception('Exception in cinform')
