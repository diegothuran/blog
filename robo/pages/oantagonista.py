# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 2956
RANK_BRAZIL = 51
NAME = 'oantagonista.com'


def get_urls():
    try:
        urls = [] 
        for i in range(1,PAGE_LIMIT):
            link = 'https://www.oantagonista.com/pagina/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='container-post-home')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[2]['href'] 
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in oantagonista')