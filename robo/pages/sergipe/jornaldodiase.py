# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 2394022
RANK_BRAZIL = 77969     
NAME = 'jornaldodiase.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://www.jornaldodiase.com.br/'
        links = ['http://www.jornaldodiase.com.br/index.php',
                'http://www.jornaldodiase.com.br/noticias.php?id=3',
                'http://www.jornaldodiase.com.br/noticias.php?id=4',
                'http://www.jornaldodiase.com.br/noticias.php?id=10',
                'http://www.jornaldodiase.com.br/noticias.php?id=20',
                'http://www.jornaldodiase.com.br/noticias.php?id=12',
                 ]
        
        for i in range(len(links)):
            req = requests.get(links[i])
            if(i==0):
                noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='noticia ')
            else:
                noticias = BeautifulSoup(req.text, "html.parser").find_all('h4')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in jornaldodiase')
