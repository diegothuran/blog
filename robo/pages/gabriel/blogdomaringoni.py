# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 10746
RANK_BRAZIL = 223 
NAME = 'revistaforum.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.revistaforum.com.br/blogs/blogdomaringoni/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h4', class_='media-heading')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in blogdomaringoni')
    

