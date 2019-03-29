# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages import PAGE_LIMIT

GLOBAL_RANK = 1306322
RANK_BRAZIL = None
NAME = 'pagina20.net'

def get_urls():
    try:
        urls = [] 
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'http://pagina20.net/v2/category/economia/'
            else:
                link = 'http://pagina20.net/v2/category/economia/page/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='card painel-noticias2')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in pagina20_economia')

