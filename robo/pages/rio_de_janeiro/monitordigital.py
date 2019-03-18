# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1114340
RANK_BRAZIL = 57138    
NAME = 'monitordigital.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://monitordigital.com.br/categorias/politica',
                'https://monitordigital.com.br/categorias/internacional',
                'https://monitordigital.com.br/categorias/mercado-financeiro',
                'https://monitordigital.com.br/categorias/rio-de-janeiro',
                'https://monitordigital.com.br/categorias/sao-paulo',
                'https://monitordigital.com.br/categorias/empresas',
                'https://monitordigital.com.br/categorias/conjuntura'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='titulo')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in monitordigital')
