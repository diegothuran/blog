# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 7261017 
RANK_BRAZIL = None    
NAME = 'correiodepernambuco.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://correiodepernambuco.com.br/brasil/',
                'https://correiodepernambuco.com.br/politica/',
                'https://correiodepernambuco.com.br/economia/',
                'https://correiodepernambuco.com.br/internacional/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='entry-title')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in correiodepernambuco')
