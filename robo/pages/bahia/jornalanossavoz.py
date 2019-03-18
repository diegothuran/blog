# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 9391255
RANK_BRAZIL = None
NAME = 'sertaohoje.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://www.sertaohoje.com.br/'
        for i in range(1, PAGE_LIMIT):
            if(i == 1):
                link = 'http://www.sertaohoje.com.br'
            else:
                link = 'http://www.sertaohoje.com.br/noticias/' + str(i)
                
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_="blog")
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in sertaohoje')