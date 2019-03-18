# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1211621
RANK_BRAZIL = 37603    
NAME = 'gazetasp.com.br'


def get_urls():
    try:
        root = 'https://www.gazetasp.com.br'
        urls = [] 
        links = [
                'https://www.gazetasp.com.br/ultimas-noticias',
                'https://www.gazetasp.com.br/servicos',
                'https://www.gazetasp.com.br/capital',
                'https://www.gazetasp.com.br/grande-sao-paulo',
                'https://www.gazetasp.com.br/estado',
                'https://www.gazetasp.com.br/brasil',
                'https://www.gazetasp.com.br/mundo',
                'https://www.gazetasp.com.br/litoral',
                'https://www.gazetasp.com.br/vale-do-ribeira'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='catItemHeader')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in gazetasp')
