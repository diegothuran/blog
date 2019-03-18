# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 136374
RANK_BRAZIL = 4433    
NAME = 'agorarn.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://agorarn.com.br/ultimas/',
                'http://agorarn.com.br/politica/',
                'http://agorarn.com.br/categoria/cidades/',
                'http://agorarn.com.br/categoria/policia/',
                'http://agorarn.com.br/categoria/economia/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-md-8 col-sm-7 col-xs-7')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in agorarn')
