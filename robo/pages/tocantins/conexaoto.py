# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 230588
RANK_BRAZIL = 10997    
NAME = 'conexaoto.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://conexaoto.com.br'
        links = [
                'https://conexaoto.com.br/editoria/estado',
                'https://conexaoto.com.br/editoria/politica',
                'https://conexaoto.com.br/editoria/policia',
                'https://conexaoto.com.br/editoria/economia'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='item')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[1]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in conexaoto')
