# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 178921
RANK_BRAZIL = 5687
NAME = 'jornaldocomercio.com'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.jornaldocomercio.com/index.php?id=/ultimas_noticias/index.php'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find('div', class_='col-md-8 col-sm-12').find_all('a', href=True)
        for noticia in noticias:
            href = "https://www.jornaldocomercio.com" + noticia['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornaldocomercio')
    
