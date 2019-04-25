# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 2918 
RANK_BRAZIL = 60 
NAME = 'r7.com'


def get_urls():
    try:
        urls = [] 
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'https://noticias.r7.com/noticias'
            else:
                link = 'https://noticias.r7.com/noticias?page=' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='listing-title')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href'] 
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in r7')
