# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 66680
RANK_BRAZIL = 2233    
NAME = 'folhape.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://www.folhape.com.br'
        links = [
                'https://www.folhape.com.br/noticias/',
                'https://www.folhape.com.br/noticias/noticias/brasil/',
                'https://www.folhape.com.br/noticias/noticias/cotidiano/',
                'https://www.folhape.com.br/noticias/noticias/mundo/',
                'https://www.folhape.com.br/economia/',
                'https://www.folhape.com.br/politica/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('section', class_='box-featured featured-noticias large')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in folhape')
