# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')
from bs4 import BeautifulSoup
import requests
from robo.pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 9755719
RANK_BRAZIL = None
NAME = 'jornalcorreiocapixaba.com.br'


def get_urls():
    try:
        urls = [] 
        for i in range(PAGE_LIMIT):
            link = 'http://jornalcorreiocapixaba.com.br/pt-BR/publicacoes/?page=' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='block_topic_post_feature')
            noticias += BeautifulSoup(req.text, "html.parser").find_all('article', class_='block_news_post')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornalcorreiocapixaba')
