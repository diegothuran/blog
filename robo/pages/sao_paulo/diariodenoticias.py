# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 4718953
RANK_BRAZIL = None   
NAME = 'diariodenoticias.com.br'


def get_urls():
    try:
        root = 'http://www.diariodenoticias.com.br'
        urls = [] 
        links = [
                'http://www.diariodenoticias.com.br/politica',
                'http://www.diariodenoticias.com.br/economia',
                'http://www.diariodenoticias.com.br/internacional',
                'http://www.diariodenoticias.com.br/geral'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='item')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('section', class_='col-xs-12 col-sm-4 col-md-3 pad-0')
            
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-xs-12 col-sm-6 col-md-3 pad-0')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-xs-12 col-sm-6 col-md-4 pad-l-15 xs-pad-l-0 xs-pad-t-15')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-xs-12 col-sm-6 col-md-2 pad-l-0 xs-pad-t-15 xs-pad-b-15 pad-t-15')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-xs-12 col-sm-6 col-md-4 pad-l-0 xs-pad-t-15 xs-pad-b-15 pad-t-15')
            
            'ch-index pad-t-0 xs-pad-l-0' 
            
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in diariodenoticias')
