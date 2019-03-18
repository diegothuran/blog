# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 46036
RANK_BRAZIL = 1567    
NAME = 'midiamax.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.midiamax.com.br/ultimas-noticias/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='title')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in midiamax')
