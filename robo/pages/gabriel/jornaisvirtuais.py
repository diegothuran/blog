# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 7305118
RANK_BRAZIL = None
NAME = 'jornaisvirtuais.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.jornaisvirtuais.com.br/category/noticias/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='entry-content clearfix')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornaisvirtuais')
    
