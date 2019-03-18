# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = None
RANK_BRAZIL = None   
NAME = 'folhamg.com'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.folhamg.com/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='title')
            
            for noticia in noticias:
                try:
                    href = noticia.find_all('a', href=True)[0]['href']
                    urls.append(href)
                except:
                    pass
                
        return urls
    except:
        raise Exception('Exception in folhamg')
