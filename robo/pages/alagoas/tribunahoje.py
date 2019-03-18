# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 598217
RANK_BRAZIL = 25626 
NAME = 'tribunahoje.com'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://tribunahoje.com/editorial/brasil/',
                'https://tribunahoje.com/editorial/politica/',
                'https://tribunahoje.com/editorial/policia/',
                'https://tribunahoje.com/editorial/mundo/',
                'https://tribunahoje.com/editorial/economia/'
            ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-sm-7')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href'] 
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in tribunahoje')

