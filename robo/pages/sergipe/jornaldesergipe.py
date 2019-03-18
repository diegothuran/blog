# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 4364784
RANK_BRAZIL = None    
NAME = 'jornaldesergipe.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://jornaldesergipe.com.br/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='mvp-blog-story-wrap left relative infinite-post')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in jornaldesergipe')
