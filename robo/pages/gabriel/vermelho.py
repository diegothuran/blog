# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests
from robo.pages import PAGE_LIMIT

GLOBAL_RANK = 83470
RANK_BRAZIL = 2512
NAME = 'vermelho.org.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://www.vermelho.org.br/'
        
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'http://www.vermelho.org.br/ultimas.php'
            else:
                link = 'http://www.vermelho.org.br/ultimas.php?pagina=' + str(i)
        
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='categoria_item ')
            for noticia in noticias:
                try:
                    href = noticia.find_all('a', href=True)[0]['href']
                    full_link = root + href
                    print(full_link)
        #             print(href)
                    urls.append(full_link)
                except:
                    pass
        return urls
    except:
        raise Exception('Exception in vermelho')

# print(get_urls())

