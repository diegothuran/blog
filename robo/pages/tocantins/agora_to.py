# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 6172405
RANK_BRAZIL = None    
NAME = 'agora-to.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.agora-to.com.br/noticias-politica.php',
                'http://www.agora-to.com.br/noticias-policia.php',
                'http://www.agora-to.com.br/noticias-tocantins.php',
                'http://www.agora-to.com.br/noticias-geral.php'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='news')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in agora_to')
