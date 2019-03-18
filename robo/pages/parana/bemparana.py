# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 68920
RANK_BRAZIL = 2194    
NAME = 'bemparana.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'https://www.bemparana.com.br'
        links = [
                'https://www.bemparana.com.br/noticia/term/regiao-metropolitana',
                'https://www.bemparana.com.br/noticia/term/parana',
                'https://www.bemparana.com.br/noticia/term/brasil',
                'https://www.bemparana.com.br/noticia/term/mundo',
                'https://www.bemparana.com.br/noticia/term/politica',
                'https://www.bemparana.com.br/noticia/term/economia'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in bemparana')
