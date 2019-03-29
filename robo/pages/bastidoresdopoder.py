# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages import PAGE_LIMIT

GLOBAL_RANK = 7426845
RANK_BRAZIL = None
NAME = 'bastidoresdopoder.com.br'

def get_urls():
    try:  
        urls = []  
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'http://www.bastidoresdopoder.com.br/'
                req = requests.get(link)
                noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='box-post-content')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='slide slide-1')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='slide slide-2')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='slide slide-3')
            else:
                link = 'http://www.bastidoresdopoder.com.br/page/' + str(i)
                req = requests.get(link)
                noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='box-post-content')
            
            for noticia in noticias:
    #             print(noticia.find_all('a', href=True)[0]['href'])
                urls.append(noticia.find_all('a', href=True)[0]['href'])
        return urls
    except:
        raise Exception('Exception in bastidoresdopoder')
