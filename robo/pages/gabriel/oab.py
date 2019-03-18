# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 97024
RANK_BRAZIL = 3100
NAME = 'oab.org.br'

def get_urls():
    try:
        urls = [] 
        
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'https://www.oab.org.br/noticias'
            else:
                link = 'https://www.oab.org.br/noticias/' + str(i)
        
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h4')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                if('http://www.youtube.com/watch' not in href):
                    print(href)
                    urls.append(href)
        return urls
    except:
        raise Exception('Exception in oab')

# print(get_urls())
