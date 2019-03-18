# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 3916135
RANK_BRAZIL = None    
NAME = 'correiodenoticia.com.br'

def get_urls():
    try:
        urls = []
        root = 'http://www.correiodenoticia.com.br' 
        links = [
                'http://www.correiodenoticia.com.br/index.php/editoriais/municipios',
                'http://www.correiodenoticia.com.br/index.php/editoriais/destaque',
                'http://www.correiodenoticia.com.br/index.php/editoriais/politica',
                'http://www.correiodenoticia.com.br/index.php/editoriais/economia',
                'http://www.correiodenoticia.com.br/index.php/editoriais/cultura',
                'http://www.correiodenoticia.com.br/index.php/editoriais/municipios',
                'http://www.correiodenoticia.com.br/index.php/editoriais/policica',
                'http://www.correiodenoticia.com.br/index.php/editoriais/nacional',
                'http://www.correiodenoticia.com.br/index.php/editoriais/mundo'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h2')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in correiodenoticia')
