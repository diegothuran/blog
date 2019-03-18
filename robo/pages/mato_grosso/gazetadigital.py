# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 91845
RANK_BRAZIL = 3163   
NAME = 'gazetadigital.com.br'


def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.gazetadigital.com.br/editorias/politica-de-mt/',
                'http://www.gazetadigital.com.br/editorias/judiciario/',
                'http://www.gazetadigital.com.br/editorias/economia/',
                'http://www.gazetadigital.com.br/editorias/cidades/',
                'http://www.gazetadigital.com.br/editorias/policia/',
                'http://www.gazetadigital.com.br/editorias/politica-nacional/',
                'http://www.gazetadigital.com.br/editorias/brasil/',
                'http://www.gazetadigital.com.br/editorias/mundo/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-xs-10 col-sm-10 col-md-10 col-lg-10')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in gazetadigital')
