# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')

from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 13683
RANK_BRAZIL = 351  
NAME = 'noticiasdatv.uol.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://noticiasdatv.uol.com.br'
        
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'https://noticiasdatv.uol.com.br/todas-as-noticias/'
            else:
                link = 'https://noticiasdatv.uol.com.br/todas-as-noticias/?pagina=' + str(i)
                
        
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='ultima_noticia big mb10')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-md-4')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-md-3')
            for noticia in noticias:
                try:
                    href = noticia.find_all('a', href=True)[0]['href']
                    full_link = root + href
#                     print(full_link)
                    urls.append(full_link)
                except:
                    pass
        return urls
    except:
        raise Exception('Exception in noticiasdatv')

# print(get_urls())


