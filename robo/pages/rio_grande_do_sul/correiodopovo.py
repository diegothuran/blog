# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 35259
RANK_BRAZIL = 1087      
NAME = 'correiodopovo.com.br'

def get_urls():
    try:
        root = 'http://www.correiodopovo.com.br'
        urls = [] 
        links = [
                'http://www.correiodopovo.com.br/busca/?Sessao=Noticias&ED=Cidades',
                'http://www.correiodopovo.com.br/busca/?Sessao=Noticias&ED=Economia',
                'http://www.correiodopovo.com.br/busca/?Sessao=Noticias&ED=Geral',
                'http://www.correiodopovo.com.br/busca/?Sessao=Noticias&ED=Mundo',
                'http://www.correiodopovo.com.br/busca/?Sessao=Noticias&ED=Policia',
                'http://www.correiodopovo.com.br/busca/?Sessao=Noticias&ED=Politica',
                'http://www.correiodopovo.com.br/busca/?Sessao=Noticias&ED=Rural'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h1')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in correiodopovo')
