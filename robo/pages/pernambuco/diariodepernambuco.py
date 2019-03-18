# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 44227
RANK_BRAZIL = 1770    
NAME = 'diariodepernambuco.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.diariodepernambuco.com.br/ultimas/capa_ultimas/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('a', class_='destaque')
            for noticia in noticias:
                href = noticia['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in diariodepernambuco')
