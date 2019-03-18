# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 3853959
RANK_BRAZIL = None
NAME = 'folhasertaneja.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://www.folhasertaneja.com.br'
        
        req = requests.get(root)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h3')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            full_link = root + href 
#             print(full_link)
            urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in folhasertaneja')
