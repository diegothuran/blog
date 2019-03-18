# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 936 
RANK_BRAZIL = 25   
NAME = 'exame.abril.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://exame.abril.com.br/ultimas-noticias/'
        for i in range(PAGE_LIMIT):
            if(i == 0):
                link = 'https://www.gazetadopovo.com.br/ultimas-noticias/'
            else:
                link = 'https://www.gazetadopovo.com.br/ultimas-noticias/?offset=' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='c-chamada lista-ordenada ultimas-chamadas')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in exame')
