
# coding: utf-8
import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 148 
RANK_BRAZIL = 5 
NAME = 'g1.globo.com'

def get_urls():
    try:
        urls = [] 

        links = ['https://g1.globo.com/politica/eleicoes/2018/', 
                 'https://g1.globo.com/df/distrito-federal/eleicoes/2018/',
                 'https://g1.globo.com/go/goias/eleicoes/2018/',
                 'https://g1.globo.com/mt/mato-grosso/eleicoes/2018/',
                 'https://g1.globo.com/ms/mato-grosso-do-sul/eleicoes/2018/',
                 'https://g1.globo.com/al/alagoas/eleicoes/2018/',
                 'https://g1.globo.com/ba/bahia/eleicoes/2018/',
                 'https://g1.globo.com/ce/ceara/eleicoes/2018/',
                 'https://g1.globo.com/ma/maranhao/eleicoes/2018/',
                 'https://g1.globo.com/pb/paraiba/eleicoes/2018/',
                 'https://g1.globo.com/pe/pernambuco/eleicoes/2018/',
                 'https://g1.globo.com/pi/piaui/eleicoes/2018/',
                 'https://g1.globo.com/rn/rio-grande-do-norte/eleicoes/2018/',
                 'https://g1.globo.com/se/sergipe/eleicoes/2018/',
                 'https://g1.globo.com/ac/acre/eleicoes/2018/',
                 'https://g1.globo.com/ap/amapa/eleicoes/2018/',
                 'https://g1.globo.com/am/amazonas/eleicoes/2018/',
                 'https://g1.globo.com/pa/para/eleicoes/2018/',
                 'https://g1.globo.com/ro/rondonia/eleicoes/2018/',
                 'https://g1.globo.com/rr/roraima/eleicoes/2018/',
                 'https://g1.globo.com/to/tocantins/eleicoes/2018/',
                 'https://g1.globo.com/es/espirito-santo/eleicoes/2018/',
                 'https://g1.globo.com/mg/minas-gerais/eleicoes/2018/',
                 'https://g1.globo.com/rj/rio-de-janeiro/eleicoes/2018/',
                 'https://g1.globo.com/sp/sao-paulo/eleicoes/2018/',
                 'https://g1.globo.com/pr/parana/eleicoes/2018/',
                 'https://g1.globo.com/rs/rio-grande-do-sul/eleicoes/2018/',
                 'https://g1.globo.com/sc/santa-catarina/eleicoes/2018/'
            ]
        
        for link in links:
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='feed-post bstn-item-shape type-materia')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href'] 
    #             print(href)
                urls.append(href)
            
        return urls
    except:
        raise Exception('Exception in globo_eleicoes')
