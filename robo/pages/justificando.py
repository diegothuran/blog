# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages import PAGE_LIMIT

GLOBAL_RANK = 201490
RANK_BRAZIL = 4309   
NAME = 'justificando.com'

def get_urls():
    try:
        urls = [] 
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'http://www.justificando.com/categoria/noticias/'
            else:
                link = 'http://www.justificando.com/categoria/noticias/page/2/'
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h4', class_='entry-title entry-title-left')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in justificando')
