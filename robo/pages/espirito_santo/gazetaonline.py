# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 23305
RANK_BRAZIL = 730
NAME = 'gazetaonline.com.br'


def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.gazetaonline.com.br/noticias/cidades',
                'https://www.gazetaonline.com.br/noticias/policia',
                'https://www.gazetaonline.com.br/noticias/economia',
                'https://www.gazetaonline.com.br/noticias/politica',
                'https://www.gazetaonline.com.br/noticias/brasil',
                'https://www.gazetaonline.com.br/noticias/mundo',
                'https://www.gazetaonline.com.br/sul',
                'https://www.gazetaonline.com.br/norte'
            ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='module cat-noticias ')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in gazetaonline')

