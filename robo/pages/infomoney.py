# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 5435
RANK_BRAZIL = 137   
NAME = 'infomoney.com.br'

def get_urls():
    try:
        urls = []
        root = 'https://www.infomoney.com.br'
        
        for i in range(1,PAGE_LIMIT):
            if(i == 1):
                link = 'https://www.infomoney.com.br/ultimas-noticias'
            else:
                link = 'https://www.infomoney.com.br/ultimas-noticias/pagina/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='section-box-secondary-container-description')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in infomoney')
