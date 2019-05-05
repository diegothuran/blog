# coding: utf-8

import sys
sys.path.insert(0, '../../../blog')

from robo.postagem import util_pessoas
from robo.pages.util import load_pages


""" post """
while(True):
    for page in load_pages.PAGES_UOL:
        try:
            urls = page.get_urls()
            news_from_globo = False
            name_site = page.NAME
            for url in urls:
                print('\n' + url)
                util_pessoas.news_from_link(url, name_site)

        except Exception as e:
            print(e)
            pass


# """ post """
# # primeira_vez = True
# for page in load_pages.PAGES:
#     try:
#         urls = page.get_urls()
#         news_from_globo = False
#         primeira = True
#         for url in urls:
#             if(primeira):
#                 print('\n' + url)
#                 util_pessoas.news_from_link(url)
#             else:
#                 primeira = False
#                 print('--- primeira: ' + str(primeira))
#                 break
#  
#     except Exception as e:
#         print(e)
#         pass