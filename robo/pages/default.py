# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

root = 'https://www.gazetadopovo.com.br/'
for i in range(10):
    if(i == 0):
        link = 'https://www.gazetadopovo.com.br/ultimas-noticias/'
    else:
        link = 'https://www.gazetadopovo.com.br/ultimas-noticias/?offset=' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='c-chamada lista-ordenada ultimas-chamadas')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        full_link = root + href 
        print(full_link)
