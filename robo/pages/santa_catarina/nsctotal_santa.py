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
                'https://www.nsctotal.com.br/santa/ultimas-noticias',
                'https://www.nsctotal.com.br/santa/categoria/politica',
                'https://www.nsctotal.com.br/santa/categoria/economia'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='sc-kUaPvJ gjMMZr sc-eMigcr StyledItem gOtrSF sc-itybZL bXEnCi sc-hGoxap Container idLKpM')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in nsctotal_santa')
