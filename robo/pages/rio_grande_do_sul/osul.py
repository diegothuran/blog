# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 170946
RANK_BRAZIL = 5684    
NAME = 'osul.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.osul.com.br/noticias/',
                'http://www.osul.com.br/noticias/rs/',
                'http://www.osul.com.br/noticias/brasil/',
                'http://www.osul.com.br/noticias/mundo/',
                'http://www.osul.com.br/noticias/geral/',
                'http://www.osul.com.br/noticias/politica/',
                'http://www.osul.com.br/noticias/economia/',
                'http://www.osul.com.br/atividades-empresariais/',
                'http://www.osul.com.br/atividades-rurais/',
                 ]
        
        for i in range(len(links)):
            req = requests.get(links[i])
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='entry-title')
            if(i == 0):
                noticias += BeautifulSoup(req.text, "html.parser").find_all('h3', class_='large-font')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('h3', class_='small-font')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in osul')
