# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 691022
RANK_BRAZIL = 17938    
NAME = 'horadopovo.org.br'


def get_urls():
    try:
        urls = [] 
        for i in range(1,PAGE_LIMIT):
            if(i ==1):
                link = 'https://horadopovo.org.br/author/horadopovo/'
            else:
                link = 'https://horadopovo.org.br/author/horadopovo/page/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='category-item-2')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in horadopovo')
