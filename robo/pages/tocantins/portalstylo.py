# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 1373507
RANK_BRAZIL = 49879     
NAME = 'portalstylo.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://www.portalstylo.com.br'
        
        for i in range(PAGE_LIMIT):
            link = 'http://www.portalstylo.com.br/noticias?&pg=' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='grid_6 block_default_images alpha')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in portalstylo')
