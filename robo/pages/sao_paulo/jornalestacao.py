# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 6063975
RANK_BRAZIL = None 
NAME = 'jornalestacao.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.jornalestacao.com.br/portal/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='content-carousel')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='entry-content-media')
            
            for noticia in noticias:
                try:
                    href = noticia.find_all('a', href=True)[0]['href']
                    if('2017' not in href):
                        urls.append(href)
                except:
                    pass
        return urls
    except:
        raise Exception('Exception in jornalestacao')
