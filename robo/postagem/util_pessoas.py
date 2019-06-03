# coding: utf-8

import sys, os
sys.path.insert(0, '../../../blog')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
import django
django.setup()

import pandas as pd
import urllib
import datetime

from newsplease import NewsPlease
from bs4 import BeautifulSoup

from robo.lexical_analyzer_package import pessoas_lexical
from robo.postagem import pessoas_post 

from robo.Util import util

from articles.models import Article
from category.models import Category

def news_from_link(ref_link, name_site):
    info = {'title': [], 'slug': [], 'body': [], 'date': [], 'thumb': [], 'link': [], 'categories': []}
    article = NewsPlease.from_url(ref_link)
    if (article is not None):
        info['title'].append(article.title)
        info['slug'].append(util.slugify_title(article.title))
        info['body'].append(article.text)
        info['link'].append(article.url)
        
        if((article.date_publish == None) or (article.date_publish > datetime.datetime.now())):
            info['date'].append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            info['date'].append(article.date_publish)
        
        path_image = article.image_url
        print(path_image)
        if path_image == '' or path_image == None:
            info['thumb'].append(0)
        else:
            info['thumb'].append(util.download_and_move_image(article.image_url))
        
        try:
            print(info['title'])    
            if(not Article.objects.filter(slug = info['slug'][0]).exists()):
                print('news_in_db: False')
                categories = pessoas_lexical.django_lexical_corpus_and_title(article.title, article.text)
                all_categorias = Category.objects.all()
                info['categories'] = util.django_get_categories_idx(categories[0], all_categorias)
                pessoas_post.post_news(info)
            else:
                print('news_in_db: True')
        except:
            print('Empty News')
        