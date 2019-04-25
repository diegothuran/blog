# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')

from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 15823
RANK_BRAZIL = 423  
NAME = 'www.valor.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://www.valor.com.br'
        
        for i in range(0,PAGE_LIMIT):
            if(i == 0):
                link = 'https://www.valor.com.br/ultimas-noticias'
            else:
                link = 'https://www.valor.com.br/ultimas-noticias?page=' + str(i)
        
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='title2')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                print(full_link)
                urls.append(full_link)
        return urls
    except:
        raise Exception('Exception in valor')

# print(get_urls())
