# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages import PAGE_LIMIT

GLOBAL_RANK = 112626
RANK_BRAZIL = 3957 
NAME = 'cadaminuto.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://www.cadaminuto.com.br'
        for i in range(1, PAGE_LIMIT):
            if(i == 1):
                link = 'https://www.cadaminuto.com.br/noticias'
            else:
                link = 'https://www.cadaminuto.com.br/noticias?page=' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-md-4')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in cadaminuto')
                
