# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 444311
RANK_BRAZIL = 19803
NAME = 'jornalfolhadoestado.com'


def get_urls():
    try:
        urls = [] 
        root = 'https://www.jornalfolhadoestado.com'
        links = [
                'https://www.jornalfolhadoestado.com/secoes/5/internacional',
                'https://www.jornalfolhadoestado.com/secoes/7/geral',
                'https://www.jornalfolhadoestado.com/secoes/10/politica',
                'https://www.jornalfolhadoestado.com/secoes/11/seguranca',
                'https://www.jornalfolhadoestado.com/secoes/19/economia',
                'https://www.jornalfolhadoestado.com/secoes/20/brasil',
                'https://www.jornalfolhadoestado.com/secoes/21/tv-e-famosos'
            ]
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='margemt')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornalfolhadoestado')
