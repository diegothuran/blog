# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 11740
RANK_BRAZIL = 353    
NAME = 'destakjornal.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://www.destakjornal.com.br'
        links = [
                'https://www.destakjornal.com.br/ultima-hora',
                'https://www.destakjornal.com.br/brasil',
                'https://www.destakjornal.com.br/seu-valor',
                'https://www.destakjornal.com.br/mundo',
                'https://www.destakjornal.com.br/cidades'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='noticiaRow')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in destakjornal')
