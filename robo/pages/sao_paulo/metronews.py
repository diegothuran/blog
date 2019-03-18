# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 557366
RANK_BRAZIL = 23002    
NAME = 'metronews.com.br'


def get_urls():
    try:
        root = 'https://metronews.com.br'
        urls = [] 
        links = [
#                 'https://metronews.com.br/',
#                 'https://metronews.com.br/nacional',
                'https://metronews.com.br/eeconomia',
                'https://metronews.com.br/egeral',
                'https://metronews.com.br/einternacional',
                'https://metronews.com.br/epolitica'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='article-title')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in metronews')
