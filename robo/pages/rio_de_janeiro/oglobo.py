# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 149
RANK_BRAZIL = 5    
NAME = 'oglobo.globo.com'

def get_urls():
    try:
        urls = [] 
        links = [
                'https://oglobo.globo.com/rio/',
                'https://oglobo.globo.com/brasil/',
                'https://oglobo.globo.com/mundo/',
                'https://oglobo.globo.com/economia/'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='titulo ')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='inner-border')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='inner-border ')
            
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = link + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in oglobo')
