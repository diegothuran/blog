# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 490286
RANK_BRAZIL = 17614 
NAME = 'convergenciadigital.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://www.convergenciadigital.com.br'
        link = 'http://www.convergenciadigital.com.br/cgi/cgilua.exe/sys/start.htm?UserActiveTemplate=site&tpl=home'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='glidecontent')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h2')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h3')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h3', class_='tv_dir')
        
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
            full_link = root + href
#             print(href)
            urls.append(full_link)
        return urls
    except:
        raise Exception('Exception in convergenciadigital')

# print(get_urls())

