# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 562555
RANK_BRAZIL = 37561    
NAME = 'correiodobrasil.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.correiodobrasil.com.br/Cat/politica/',
                'https://www.correiodobrasil.com.br/Cat/negocios/',
                'https://www.correiodobrasil.com.br/Cat/brasil/',
                'https://www.correiodobrasil.com.br/Cat/mundo/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='entry-title')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in correiodobrasil')
