# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 4460065
RANK_BRAZIL = None    
NAME = 'tribunadenoticias.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.tribunadenoticias.com.br/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='post-title entry-title')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in tribunadenoticias')
