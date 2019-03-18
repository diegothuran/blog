# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 11740
RANK_BRAZIL = 353    
NAME = 'em.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.em.com.br/gerais/',
                'https://www.em.com.br/politica/',
                'https://www.em.com.br/economia/',
                'https://www.em.com.br/nacional/',
                'https://www.em.com.br/internacional/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h4', class_='txt-serif mt-0 mb-10')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in em')
