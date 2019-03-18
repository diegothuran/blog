# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 2884
RANK_BRAZIL = 178     
NAME = 'gazetadopovo.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://www.gazetadopovo.com.br'
        links = [
                'https://www.gazetadopovo.com.br/politica/',
                'https://www.gazetadopovo.com.br/economia/',
                'https://www.gazetadopovo.com.br/curitiba/',
                'https://www.gazetadopovo.com.br/vida-publica/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='c-chamada lista-chamada')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                if(root not in href):
                    full_link = root + href
                    urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in gazetadopovo')
