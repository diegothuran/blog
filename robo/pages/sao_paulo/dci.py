# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 219050
RANK_BRAZIL = 7718
NAME = 'dci.com.br'

def get_urls():
    try:
        root = 'https://www.dci.com.br'
        urls = [] 
        links = [
                'https://www.dci.com.br/',
                'https://www.dci.com.br/mundo',
                'https://www.dci.com.br/economia',
                'https://www.dci.com.br/politica',
                'https://www.dci.com.br/financas',
                'https://www.dci.com.br/dci-sp'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='titulo')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
        return urls
    except:
        raise Exception('Exception in dci')
