# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 282596
RANK_BRAZIL = 9486    
NAME = 'correiodaparaiba.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://correiodaparaiba.com.br/geral/',
                'https://correiodaparaiba.com.br/politica/',
                'https://correiodaparaiba.com.br/economia/',
                'https://correiodaparaiba.com.br/cidades/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-xs-12 col-sm-6 col-md-3')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in correiodaparaiba')
