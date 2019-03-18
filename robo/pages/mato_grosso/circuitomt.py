# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 255642
RANK_BRAZIL = None   
NAME = 'circuitomt.com.br'


def get_urls():
    try:
        root = 'http://circuitomt.com.br/'
        urls = [] 
        links = [
                'http://circuitomt.com.br/editorias/agronegocio.html',
                'http://circuitomt.com.br/editorias/brasil.html',
                'http://circuitomt.com.br/editorias/cidades.html',
                'http://circuitomt.com.br/editorias/cultura.html',
                'http://circuitomt.com.br/editorias/economia.html',
                'http://circuitomt.com.br/editorias/geral.html',
                'http://circuitomt.com.br/editorias/juridico.html',
                'http://circuitomt.com.br/editorias/mundo.html',
                'http://circuitomt.com.br/editorias/policia.html',
                'http://circuitomt.com.br/editorias/politica.html'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='news-title')

            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in circuitomt')
