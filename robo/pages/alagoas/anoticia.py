# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 3562682
RANK_BRAZIL = None
NAME = 'anoticia.online'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.anoticia.online/category/politica/',
                'http://www.anoticia.online/category/brasil/',
                'http://www.anoticia.online/category/mundo/',
                'http://www.anoticia.online/category/policia/',
                'http://www.anoticia.online/category/economia/'
                ]
        
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='bold xt-post-title')
            for noticia in noticias:    
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in anoticia')

        
