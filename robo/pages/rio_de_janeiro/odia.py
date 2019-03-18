# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

# pegou o rank do ig
GLOBAL_RANK = 2759
RANK_BRAZIL = 71    
NAME = 'odia.ig.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://odia.ig.com.br'
        links = [
                'https://odia.ig.com.br/rio-de-janeiro',
                'https://odia.ig.com.br/eleicoes',
                'https://odia.ig.com.br/economia',
                'https://odia.ig.com.br/brasil',
                'https://odia.ig.com.br/mundo-e-ciencia'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='chamada--news chamada--photo__full')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in odia')
