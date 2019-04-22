import requests
from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from rest_framework import generics
from . import serializers

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from robo.teste import teste_db


# Create your views here.
def article_list(request):
#     articles = models.Article.objects.all().order_by('-date')
#     user_list = User.objects.all()
    article_list = models.Article.objects.all().order_by('-date')
    
#     page = request.GET.get('page', 1)
#     paginator = Paginator(article_list, 10)
#     try:
#         articles = paginator.page(page)
#     except PageNotAnInteger:
#         articles = paginator.page(1)
#     except EmptyPage:
#         articles = paginator.page(paginator.num_pages)
    return render(request, 'articles/article_list.html', {'articles': article_list})


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
    
    try:
        relevancia = teste_db.get_relevancia(article.link)
    except:
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

