# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 20011
RANK_BRAZIL = 731
NAME = 'huffpostbrasil.com'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.huffpostbrasil.com/politica/'
        root = "https://www.huffpostbrasil.com"
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='splash-inner')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='card__content')
        for noticia in noticias:
            ref_link = noticia.find_all('a', href=True)[0]['href']
            if (root not in ref_link):
                href = root + ref_link
            else:
                href = ref_link
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in huffpostbrasil')
    