# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 13027
RANK_BRAZIL = 297
NAME = 'camara.leg.br'


def get_urls():
    try:
        urls = [] 
        link = 'http://www2.camara.leg.br/camaranoticias/dinamico/ultimasNoticiasAgencia'
        req = requests.get(link)
        
        div = BeautifulSoup(req.text, "html.parser").find_all('div', id='resultadoPesquisa')    
        ultags = div[0].find_all('ul')    
        for ul in ultags:
            for li in ul.find_all('li'):
                href = li.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in camara')
