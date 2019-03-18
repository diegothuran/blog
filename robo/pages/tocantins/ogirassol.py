# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 999099
RANK_BRAZIL = 35790   
NAME = 'ogirassol.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.ogirassol.com.br/estado',
                'http://www.ogirassol.com.br/geral',
                'http://www.ogirassol.com.br/politica'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-lg-8 col-md-8 col-sm-8')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in ogirassol')
