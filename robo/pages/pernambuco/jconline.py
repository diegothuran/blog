# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 17323
RANK_BRAZIL = 609    
NAME = 'jconline.ne10.uol.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://jconline.ne10.uol.com.br/canal/cidades',
                'https://jconline.ne10.uol.com.br/canal/economia',
                'https://jconline.ne10.uol.com.br/canal/politica',
                'https://jconline.ne10.uol.com.br/canal/mundo'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='lista-noticia-item')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in jconline')
