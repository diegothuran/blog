import requests
from django.shortcuts import render, redirect
from . import models

from django.contrib.auth.decorators import login_required
from . import forms
from rest_framework import generics
from api import serializers

from robo.analytics import analises
from slugify import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from robo.lexical_analyzer_package import pessoas_lexical

from robo.Util import util
from category.models import Category

import django.db

# Create your views here.
def article_list(request):
    #django.db.close_old_connections()
#     articles = models.Article.objects.all().order_by('-date')
#     user_list = User.objects.all()
    article_list = models.Article.objects.all().order_by('-date')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(article_list, 10)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
#     return render(request, 'articles/article_list.html', {'articles': article_list})
    return render(request, 'articles/article_list.html', {'articles':articles})


def article_detail(request, slug):
    article = models.Article.objects.get(slug=slug)
    article_list = models.Article.objects.all().order_by('-date')
    most_recent = article_list[:5]
    try:
        next_article = article.get_next_by_date()
    except:
        next_article = ''
    
    try:
        previous_article = article.get_previous_by_date()
    except:
        previous_article = ''
    
#     relevancia = 3.2
    
#     try:
#         relevancia = analises.get_relevancia(article.link)
#     except:
#         relevancia = "--"
    relevancia = "--"
            
    URL = 'https://api.sharedcount.com/v1.0/'
    api_key = '8a2cccc01f801d984aa5995bc3d3594bed656a51'
    
    # https://api.sharedcount.com/v1.0/?apikey=8a2cccc01f801d984aa5995bc3d3594bed656a51&url=https%3A%2F%2Fwww.globo.com%2F  
      
    url_midia = article.link
      
    payload = {'apikey': api_key, 'url': url_midia}
    r = requests.get(URL, params=payload)
    temp = r.json()
#     print(r)
#     print(r.url)
#       
#     print(temp)
    nb_shares = temp['Facebook']['total_count']
#     next_article, previous_article = None, None
#     print(article.get_next_by_date())
#     previous_article = article.get_previous_by_date()
    return render(request, 'articles/article_detail.html', 
                  {'article': article, 'next': next_article, 'previous':previous_article, 'relevancia': relevancia,
                   'nb_shares': nb_shares, 'most_recent': most_recent})


# @login_required(login_url="/usuarios/login/")
@login_required(login_url="/accounts/login/")
def article_create(request):
    if(request.method == "POST"):
        form = forms.CreateArticle(request.POST, request.FILES)
        if(form.is_valid()):
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})


class ArticleList(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

def slug_correction(request):
    articles = models.Article.objects.all()
    for article in articles:
        article.slug = slugify(article.title)
        article.save()

def update_categories(request):
    articles = models.Article.objects.all()[1050:]
    for article in articles:
        print(article.id)
        
        categories = pessoas_lexical.django_lexical_corpus_and_title(article.title, article.body)
        all_categorias = Category.objects.all()
        categories = util.django_get_categories_idx(categories[0], all_categorias)
                
        for cat_idx in categories:
            article.categories.add(cat_idx)
