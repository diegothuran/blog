# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')

from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 1111950
RANK_BRAZIL = 24399
NAME = 'abi.org.br'

def get_urls():
    try:
        urls = [] 
        
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'http://www.abi.org.br/category/primeira-pagina/'
            else:
                link = 'http://www.abi.org.br/category/primeira-pagina/page/' + str(i)
        
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h4')
            for noticia in noticias:
                try:
                    href = noticia.find_all('a', href=True)[0]['href']
#                     print(href)
        #             full_link = root + href
                    urls.append(href)
                except:
                    pass
        return urls
    except:
        raise Exception('Exception in abi')

# print(get_urls())
