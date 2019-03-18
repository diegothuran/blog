import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 4444 
RANK_BRAZIL = 129
NAME = 'gauchazh.clicrbs.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'https://gauchazh.clicrbs.com.br/politica/eleicoes/ultimas-noticias/'
        req = requests.get(link)
        bs = BeautifulSoup(req.text, "html.parser")
        noticias = bs.find('section', class_='section-latest-page').find_all('div', class_='card')
        for noticia in noticias:
            href = 'https://gauchazh.clicrbs.com.br' + noticia.find('a', href=True)['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in gauchazh')
    