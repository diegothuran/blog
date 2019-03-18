# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1083136
RANK_BRAZIL = 46313     
NAME = 'diarioinduscom.com'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.diarioinduscom.com/conteudo/editorias/economia/',
                'http://www.diarioinduscom.com/conteudo/editorias/parana/',
                'http://www.diarioinduscom.com/conteudo/editorias/negocios/',
                'http://www.diarioinduscom.com/conteudo/editorias/nacional/',
                'http://www.diarioinduscom.com/conteudo/editorias/mundo/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='td-module-thumb')
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='item-details')
            
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in diarioinduscom')
