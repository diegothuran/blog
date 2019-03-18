# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 6107148
RANK_BRAZIL = None   
NAME = 'copopular.com.br'


def get_urls():
    try:
        root = 'http://www.copopular.com.br'
        urls = [] 
        links = [
                'http://www.copopular.com.br/agronegocio',
                'http://www.copopular.com.br/economia',
                'http://www.copopular.com.br/cidades',
                'http://www.copopular.com.br/geral',
                'http://www.copopular.com.br/policia',
                'http://www.copopular.com.br/politica'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='span9')

            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in copopular')
