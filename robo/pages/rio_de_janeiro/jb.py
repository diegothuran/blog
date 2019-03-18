# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 34502
RANK_BRAZIL = 1271     
NAME = 'jb.com.br'

def get_urls():
    try:
        root = 'https://www.jb.com.br'
        urls = [] 
        links = [
                'https://www.jb.com.br/capa/noticias',
                'https://www.jb.com.br/rio',
                'https://www.jb.com.br/pais',
                'https://www.jb.com.br/economia',
                'https://www.jb.com.br/internacional'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h1')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in jb')
