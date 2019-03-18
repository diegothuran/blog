# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 3181524
RANK_BRAZIL = None
NAME = 'jornalopiniao.net'

def get_urls():
    try:
        urls = [] 
        root = 'https://www.jornalopiniao.net'
        news_idx = ['0', '8', '16', '24']
        for i in range(len(news_idx)):
            if(i == 1):
                link = 'https://www.jornalopiniao.net/index.php/tecnologia1.html'
            else:
                link = 'https://www.jornalopiniao.net/index.php/tecnologia1.html?start=' + news_idx[i]
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='itemView groupLeading')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in jornalopiniao_economia')
