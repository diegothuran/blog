# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 54844
RANK_BRAZIL = 1795      
NAME = 'folhabv.com.br'

def get_urls():
    try:
        root = 'https://www.folhabv.com.br/' 
        urls = [] 
        links = [
                'https://www.folhabv.com.br/lista/noticia/menu/cidades/3',
                'https://www.folhabv.com.br/lista/noticia/menu/policia/5',
                'https://www.folhabv.com.br/lista/noticia/menu/politica/6'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='titulo')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='titulo-img')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in folhabv')
