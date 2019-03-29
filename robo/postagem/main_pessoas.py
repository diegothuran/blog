# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from robo.postagem import util_pessoas
from robo.pages.util import load_pages

""" post """
while(True):
    for page in load_pages.PAGES:
        try:
            urls = page.get_urls()
            news_from_globo = False
            for url in urls:
                print('\n' + url)
                util_pessoas.news_from_link(url)

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