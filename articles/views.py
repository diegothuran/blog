from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from rest_framework import generics
from . import serializers

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def article_list(request):
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
    return render(request, 'articles/article_list.html', {'articles':articles})


def article_detail(request, slug):
    article = models.Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


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

