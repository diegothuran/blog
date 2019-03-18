# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 766114
RANK_BRAZIL = 47030 
NAME = 'blogdopaulonunes.com'

def get_urls():
    try:
        urls = [] 
        link = 'http://www.blogdopaulonunes.com/v4/?cat=6'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in blogdopaulonunes')
    