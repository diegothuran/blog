# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 45874
RANK_BRAZIL = 1592     
NAME = 'tribunadonorte.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://www.tribunadonorte.com.br'
        links = [
                'http://www.tribunadonorte.com.br/',
                'http://www.tribunadonorte.com.br/natal',
                'http://www.tribunadonorte.com.br/politica',
                'http://www.tribunadonorte.com.br/economia'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='r-post-small')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in tribunadonorte')
