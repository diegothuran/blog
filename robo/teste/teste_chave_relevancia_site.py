# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import pandas as pd
import urllib
import datetime

from newsplease import NewsPlease
from bs4 import BeautifulSoup

from Model.News_with_Relevance import News_with_Relevance
from postagem.Util import download_and_move_image 

from Database import credito_table, relevancia_site_table
from lexical_analyzer_package import pessoas_lexical
from pessoas_postagem import pessoas_post

from pessoas_postagem import util_pessoas
from pages.util import load_pages


def news_from_link(ref_link, site_name):
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': [], 'site': []}
    article = NewsPlease.from_url(ref_link)
    if (article is not None):
        row['titulos'].append(article.title)
        row['noticia'].append(article.text)
        row['links'].append(article.url)
        row['abstract'].append(article.text)
#         if(article.date_publish == None):
        if((article.date_publish == None) or (article.date_publish > datetime.datetime.now())):
            row['date'].append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            row['date'].append(article.date_publish)
        path_image = article.image_url
        print(path_image)
        if path_image == '' or path_image == None:
            row['image'].append(0)
        else:
            row['image'].append(download_and_move_image(article.image_url))
        # estrutura tupla = (id, site, relevancia)
#         tupla = relevancia_site_table.select(site_name)
#         row['site'].append(str(tupla[0]))
        row['site'].append(site_name)
        news = News_with_Relevance(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'], row['site'])
        try:
            print(row['titulos'])
#             news_in_db = pessoas_table.check_news(news)
#             print('news_in_db: ' + str(news_in_db))
#             if (not news_in_db):
            row = pd.DataFrame(row)
            df, categories = pessoas_lexical.lexical_corpus_and_title(row)
            # DB categories
#             if (categories != [set()]):
            news.set_categories(categories)
            credito_table.save_news(news)
            pessoas_post.post_news(df)
        except:
            print('Empty News')


""" post """
# while(True):
for page in load_pages.PAGES:
    try:
        site_name = page.NAME
        urls = page.get_urls()
        news_from_globo = False
        for url in urls:
            print('\n' + url)
            news_from_link(url, site_name)

    except Exception as e:
        print(e)
        pass

