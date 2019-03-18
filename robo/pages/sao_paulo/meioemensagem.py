# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 81136
RANK_BRAZIL = 3020   
NAME = 'meioemensagem.com.br'


def get_urls():
    try:
        urls = [] 
        links = [
                'http://www.meioemensagem.com.br/home/ultimas-noticias'
                 ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in meioemensagem')
