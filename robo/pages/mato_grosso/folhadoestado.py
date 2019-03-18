# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1432357
RANK_BRAZIL = 75028   
NAME = 'folhadoestado.com.br'


def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.folhadoestado.com.br/',
                'http://www.folhadoestado.com.br/politica/',
                'http://www.folhadoestado.com.br/cidades/',
                'http://www.folhadoestado.com.br/policia/',
                'http://www.folhadoestado.com.br/brasil/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='entry-title')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in folhadoestado')
