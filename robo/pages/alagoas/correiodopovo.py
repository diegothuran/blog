# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from robo.pages import PAGE_LIMIT

GLOBAL_RANK = 2031641
RANK_BRAZIL = None
NAME = 'correiodopovo-al.com.br'


def get_urls():
    try:
        urls = [] 
        root = 'http://www.correiodopovo-al.com.br'
        
        for i in range(1, PAGE_LIMIT):
            if(i == 1):
                link = 'http://www.correiodopovo-al.com.br/index.php/noticias'
            else:
                link = 'http://www.correiodopovo-al.com.br/index.php/noticias/listar?pagina=' + str(i)
            req = requests.get(link)
            
            noticias = BeautifulSoup(req.text, "html.parser").find_all('a', class_='row', href=True)
            for noticia in noticias:
                href = noticia['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in correiodopovo')
