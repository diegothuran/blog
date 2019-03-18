# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1689290
RANK_BRAZIL = None
NAME = 'osamigosdopresidentelula.blogspot.com'

def get_urls():
    try:
        urls = [] 
        link = 'https://osamigosdopresidentelula.blogspot.com/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='post-title entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in osamigosdopresidentelula')
    
