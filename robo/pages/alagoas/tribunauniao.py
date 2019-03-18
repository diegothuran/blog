# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 2208945
RANK_BRAZIL = None
NAME = 'tribunauniao.com.br'


def get_urls():
    try:
        urls = [] 
        root = 'http://www.tribunauniao.com.br/'
#         news_idx = ['0', '24', '48', '72', '96', '120']
        news_idx = ['0', '24', '48']
        for i in range(len(news_idx)):
            link = 'http://www.tribunauniao.com.br/index.php/noticias/' + news_idx[i]
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-lg-6 col-md-6 col-sm-12')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in tribunauniao')
