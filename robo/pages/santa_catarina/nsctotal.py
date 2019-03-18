# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 74030
RANK_BRAZIL = 2221      
NAME = 'nsctotal.com.br'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://www.nsctotal.com.br/categoria/politica',
                'https://www.nsctotal.com.br/categoria/economia'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='sc-fjmCvl ContentWrapper dNbocA')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in nsctotal')
