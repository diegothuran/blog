# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 1003571
RANK_BRAZIL = 55107
NAME = 'agazetadoacre.com'

def get_urls():
    try:
        urls = [] 
        for i in range(1, PAGE_LIMIT):
            if(i == 1):
                link = 'https://agazetadoacre.com/categoria/noticias/'
            else:
                link = 'https://agazetadoacre.com/categoria/noticias/page/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='xt-archive-post-title xt-post-title')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href'] 
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in agazetadoacre')
