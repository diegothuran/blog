# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 91361
RANK_BRAZIL = 4465     
NAME = 'ndonline.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://ndonline.com.br'
        links = [
                'https://ndonline.com.br/florianopolis/noticias'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('a', class_='titulo-card')
            
            for noticia in noticias:
                href = noticia['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in ndonline')
