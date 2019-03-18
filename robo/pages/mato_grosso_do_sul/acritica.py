# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 661390
RANK_BRAZIL = 22773   
NAME = 'acritica.net'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.acritica.net/ultimas-noticias/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('a', class_='titulos')

            for noticia in noticias:
                href = noticia['href']
                urls.append(href)                
        return urls
    except:
        raise Exception('Exception in acritica')
