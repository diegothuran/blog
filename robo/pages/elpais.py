
# coding: utf-8
import sys
sys.path.insert(0, '../../src')


from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 440 
RANK_BRAZIL = None
NAME = 'brasil.elpais.com'


# def format_date(raw_date):
#     formated_date = datetime.datetime.strptime(raw_date, ' %d/%m/%Y %Hh%M ').strftime("%Y-%m-%d %H:%M:%S")
#     return formated_date

def get_urls():
    try:
        urls = [] 
        link = 'https://brasil.elpais.com/tag/elecciones_brasil/a'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='articulo__interior')
        for noticia in noticias:
            try:
                set_h2 = noticia.find_all('h2', class_='articulo-titulo')
                for h2 in set_h2:
                    internal_link = noticia.find_all('a', href=True)
                    ref = internal_link[0]['href']
                ref = 'https://brasil.elpais.com/' + str(ref)
                urls.append(ref)
        
            except:
                try:
                    internal_link = noticia.find_all('a', class_='enlace', href=True)
                    if(internal_link == []):
                        pass
                    else:
                        for temp in internal_link:
                            ref = temp['href']
                        ref = 'https:' + str(ref)
                        urls.append(ref)
                except:
                    pass
        
        return urls
    except:
        raise Exception('Exception in elpais')

if __name__ == '__main__':
    links = get_urls()
    print(links)
