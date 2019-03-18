# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 658920
RANK_BRAZIL = 31480     
NAME = 'jornaldoonibusdecuritiba.com.br'

def get_urls():
    try:
        urls = [] 
        root = 'http://www.jornaldoonibusdecuritiba.com.br'
        links = [
                'http://www.jornaldoonibusdecuritiba.com.br/editoria/1/geral',
                'http://www.jornaldoonibusdecuritiba.com.br/editoria/2/cidade',
                'http://www.jornaldoonibusdecuritiba.com.br/editoria/3/regiao-metropolitana',
                'http://www.jornaldoonibusdecuritiba.com.br/editoria/4/politica',
                'http://www.jornaldoonibusdecuritiba.com.br/editoria/7/policial'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='bloco arquivo-bloco')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
                urls.append(full_link)
                
        return urls
    except:
        raise Exception('Exception in jornaldoonibusdecuritiba')
