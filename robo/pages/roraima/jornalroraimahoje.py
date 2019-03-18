# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 3518276
RANK_BRAZIL = None     
NAME = 'jornalroraimahoje.com.br'

def get_urls():
    try:
        root = 'http://www.jornalroraimahoje.com.br'
        urls = [] 
        links = [
                'http://www.jornalroraimahoje.com.br/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='g-article-read-more')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in jornalroraimahoje')
