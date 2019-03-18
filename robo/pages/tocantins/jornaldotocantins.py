# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 329470
RANK_BRAZIL = 15610    
NAME = 'jornaldotocantins.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://www.jornaldotocantins.com.br'
        links = [
                'https://www.jornaldotocantins.com.br/editorias/estado',
                'https://www.jornaldotocantins.com.br/editorias/noticias'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='title libre-baskerville')

            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in jornaldotocantins')
