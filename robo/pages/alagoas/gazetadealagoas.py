# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

#based on the rank of globo
GLOBAL_RANK = 147 
RANK_BRAZIL = 5
NAME = 'gazetaweb.globo.com/gazetadealagoas'

def get_urls():
    try:
        urls = [] 
        root = 'https://gazetaweb.globo.com/gazetadealagoas/'
        
        links = [
                'https://gazetaweb.globo.com/gazetadealagoas/editoria.php?c=9',
                'https://gazetaweb.globo.com/gazetadealagoas/editoria.php?c=11',
                'https://gazetaweb.globo.com/gazetadealagoas/editoria.php?c=12',
                'https://gazetaweb.globo.com/gazetadealagoas/editoria.php?c=14',
                'https://gazetaweb.globo.com/gazetadealagoas/editoria.php?c=15',
                'https://gazetaweb.globo.com/gazetadealagoas/editoria.php?c=16',
                ]
        noticias = None
        for link in links:
            req = requests.get(link)
            if(noticias is None):
                noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-xs-12')
            else:
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-xs-12')
            for noticia in noticias:
                try:
                    href = noticia.find_all('a', href=True)[0]['href']
                    full_link = root + href 
#                     print(full_link)
                    urls.append(full_link)
                    href = noticia.find_all('a', href=True)[1]['href']
                    full_link = root + href 
#                     print(full_link)
                    urls.append(full_link)
                except:
                    pass
        
        return urls
    except:
        raise Exception('Exception in gazetadealagoas')
