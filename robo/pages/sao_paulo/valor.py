# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 15823
RANK_BRAZIL = 423  
NAME = 'valor.com.br'


def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.valor.com.br/',
                'https://www.valor.com.br/brasil',
                'https://www.valor.com.br/politica',
                'https://www.valor.com.br/financas',
                'https://www.valor.com.br/empresas',
                'https://www.valor.com.br/agro',
                'https://www.valor.com.br/internacional'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='teaser-title')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                if('https' in href):
                    urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in valor')
    