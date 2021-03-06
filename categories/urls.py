"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views

app_name = 'categories'

# from category.models import Category
# categorias = Category.objects.all()
# categorias[0].article_set.all()
# cat = categorias[0]
# cat.parent
# category = Category.objects.get(slug='cat')
# category.id

# from articles.models import Article
# articles = Article.objects.all()
# artigo = articles[4]
# nomes = [category.title for category in artigo.categories.all()]

urlpatterns = [
#     path('', views.article_list, name='list'),
    path('filtrar/', views.category_filter, name='filter'), 
    path('criar/', views.category_create, name='create'), 
    path('listar/', views.CategoryList.as_view(), name='list'),
    re_path('(?P<slug>[\w-]+)/$', views.category_detail, name='detail'),
]
