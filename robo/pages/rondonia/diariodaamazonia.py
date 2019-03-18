# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 335387   
RANK_BRAZIL = 9697      
NAME = 'diariodaamazonia.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.diariodaamazonia.com.br/categorias/diariodaamazonia/geral/?dinamico',
                'https://www.diariodaamazonia.com.br/categorias/diariodaamazonia/policia-diario-da-amazonia-2/?dinamico',
                'https://www.diariodaamazonia.com.br/categorias/diariodaamazonia/capital/?dinamico',
                'https://www.diariodaamazonia.com.br/categorias/diariodaamazonia/cidades/?dinamico',
                'https://www.diariodaamazonia.com.br/categorias/diariodaamazonia/politica/?dinamico',
                'https://www.diariodaamazonia.com.br/categorias/diariodaamazonia/economia/?dinamico',
                'https://www.diariodaamazonia.com.br/categorias/diariodaamazonia/agronegocio/?dinamico'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='redetv-v2-noticias-item__titulo')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in diariodaamazonia')
