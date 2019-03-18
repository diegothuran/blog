# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 686 
RANK_BRAZIL = None
NAME = 'br.sputniknews.com'

def get_urls():
    try:
        urls = [] 
        root = 'https://br.sputniknews.com'
        links = [
                'https://br.sputniknews.com/economia/',
                'https://br.sputniknews.com/brasil/',
                'https://br.sputniknews.com/mundo/'
            ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='b-stories__title')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in sputniknews')

# print(get_urls())

# def get_urls():
#     try:
#         urls = [] 
#         link = 'https://www.huffpostbrasil.com/'
#         req = requests.get(link)
#         noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='splash-inner')
#         for noticia in noticias:
#             href = noticia.find_all('a', href=True)[0]['href']
# #             print(href)
#             urls.append(href)
#         
#         return urls
#     except:
#         raise Exception('Exception in sputniknews')
