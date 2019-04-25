# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 626700
RANK_BRAZIL = 15254
NAME = 'jornalalerta.com.br'

def get_urls():
    try:
        urls = [] 
        for i in range(1, PAGE_LIMIT):
            if(i == 0):
                link = 'https://jornalalerta.com.br/categoria/destaques/'
                req = requests.get(link)
                noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='td_module_mx5 td-animation-stack td-big-grid-post-0 td-big-grid-post td-big-thumb')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='td_module_mx6 td-animation-stack td-big-grid-post-1 td-big-grid-post td-tiny-thumb')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='td_module_mx6 td-animation-stack td-big-grid-post-2 td-big-grid-post td-tiny-thumb')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='td_module_mx6 td-animation-stack td-big-grid-post-3 td-big-grid-post td-tiny-thumb')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='td_module_mx6 td-animation-stack td-big-grid-post-4 td-big-grid-post td-tiny-thumb')
                
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='td_module_1 td_module_wrap td-animation-stack')
            else:
                link = 'https://jornalalerta.com.br/categoria/destaques/page/' + str(i)
                req = requests.get(link)
                noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='td_module_1 td_module_wrap td-animation-stack')
        
        
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornalalerta')
    
