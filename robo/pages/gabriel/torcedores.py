# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 28215
RANK_BRAZIL = 942 
NAME = 'torcedores.com'

def get_urls():
    try:
        urls = [] 
        link = 'https://www.torcedores.com/'
        
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='newsroll-posts-title')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('h2')

        for noticia in noticias:
            try:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
            except:
                pass
        return urls
    except:
        raise Exception('Exception in torcedores')

# print(get_urls())


# 
# 
# # In[2]:
# 
# 
# link = 'https://www.torcedores.com/'
# 
# 
# # In[3]:
# 
# 
# link_site = 'https://www.torcedores.com'
# 
# 
# # In[4]:
# 
# 
# req = requests.get(link)
# 
# 
# # In[12]:
# 
# 
# noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='newsroll-posts-title')
# noticias += BeautifulSoup(req.text, "html.parser").find_all('h2')
# 
# 
# # In[13]:
# 
# 
# for noticia in noticias:
#     print(noticia.find_all('a', href=True)[0]['href'])
#     ref_link = noticia.find_all('a', href=True)[0]['href']
#     print(link_site+ref_link)
#     if (link_site not in ref_link):
#         util_midia.social_news_from_link(link_site+ref_link)
#         print(link_site+ref_link)
#     else:
#         util_midia.social_news_from_link(ref_link)
#         print(ref_link)
# 
# 
# # In[7]:
# 
# 
# noticias[0]

