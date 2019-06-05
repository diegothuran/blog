#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, reverse


from robo.analytics import analises
from robo.Util import util
import datetime

from . import forms

from django.db.models import Q
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from api import serializers

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from category.models import Category
from articles.models import Article

from collections import OrderedDict
from operator import itemgetter    
import numpy as np

from robo.lexical_analyzer_package import pessoas_lexical
from background_task import background

import subprocess
import os

import django.db

# from category.models import Category
# categorias = Category.objects.all()
# categorias[0].article_set.all()
# cat = categorias[0]
# cat.parent

# from articles.models import Article
# articles = Article.objects.all()
# artigo = articles[4]
# nomes = [category.title for category in artigo.categories.all()]


word_cloud = [
        {"word":"osmar terra","freq":100.0},
        {"word":"jair bolsonaro","freq":82.3956442831216},
        {"word":"presidente eleito","freq":71.86932849364791},
        {"word":"disse","freq":64.06533575317604},
        {"word":"governo","freq":59.89110707803993},
        {"word":"futuro ministro","freq":53.72050816696915},
        {"word":"ainda","freq":51.90562613430127},
        {"word":"país","freq":48.09437386569873},
        {"word":"segundo","freq":46.098003629764065},
        {"word":"direitos humanos","freq":43.738656987295826},
        {"word":"marco aurélio","freq":41.74228675136116},
        {"word":"pasta","freq":40.653357531760435},
        {"word":"ministério trabalho","freq":40.29038112522686},
        {"word":"afirmou","freq":38.11252268602541},
        {"word":"política","freq":35.93466424682396},
        {"word":"desenvolvimento social","freq":34.84573502722323},
        {"word":"brasil","freq":34.30127041742287},
        {"word":"casa civil","freq":33.938294010889294},
        {"word":"deputado federal","freq":32.849364791288565},
        {"word":"eleito jair","freq":32.48638838475499},
        {"word":"sobre","freq":32.30490018148821},
        {"word":"ano","freq":32.30490018148821},
        {"word":"todo","freq":32.30490018148821},
        {"word":"partido","freq":31.941923774954628},
        {"word":"dia","freq":31.76043557168784},
        {"word":"paulo guedes","freq":31.21597096188748},
        {"word":"ministro cidadania","freq":30.852994555353902},
        {"word":"onyx lorenzoni","freq":30.671506352087114},
        {"word":"estado","freq":30.127041742286753},
        {"word":"ministro","freq":29.945553539019965},
        {"word":"ministério justiça","freq":28.85662431941924},
        {"word":"cidadania osmar","freq":28.13067150635209},
        {"word":"hoje","freq":27.404718693284934},
        {"word":"bolsonaro","freq":27.041742286751365},
        {"word":"além","freq":26.31578947368421},
        {"word":"bolsa família","freq":26.31578947368421},
        {"word":"terra mdb","freq":25.58983666061706},
        {"word":"governo bolsonaro","freq":25.58983666061706},
        {"word":"segurança pública","freq":24.682395644283122},
        {"word":"vai","freq":24.500907441016334},
        {"word":"ministério","freq":24.500907441016334},
        {"word":"ministério cidadania","freq":24.500907441016334},
        {"word":"nome","freq":24.137931034482758},
        {"word":"área","freq":23.049001814882033},
        {"word":"mdb rs","freq":23.049001814882033},
        {"word":"gestão","freq":22.686025408348456},
        {"word":"outro","freq":22.141560798548092},
        {"word":"geral união","freq":21.960072595281307},
        {"word":"meio ambiente","freq":21.960072595281307},
        {"word":"bolsonaro psl","freq":21.77858439201452},
        {"word":"apenas","freq":20.508166969147005},
        {"word":"novo governo","freq":20.508166969147005},
        {"word":"deputado","freq":20.326678765880217},
        {"word":"parlamentares","freq":20.326678765880217},
        {"word":"michel temer","freq":20.14519056261343},
        {"word":"programa","freq":19.96370235934664},
        {"word":"grupo","freq":19.600725952813068},
        {"word":"damares alves","freq":19.419237749546276},
        {"word":"pode ser","freq":19.056261343012704},
        {"word":"sérgio moro","freq":18.87477313974592},
        {"word":"saúde","freq":18.69328493647913},
        {"word":"futuro governo","freq":18.69328493647913},
        {"word":"agora","freq":18.51179673321234},
        {"word":"cargo","freq":18.51179673321234},
        {"word":"decisão ministro","freq":17.96733212341198},
        {"word":"político","freq":17.604355716878402},
        {"word":"quarta feira","freq":17.604355716878402},
        {"word":"ex presidente","freq":17.604355716878402},
        {"word":"projeto","freq":17.422867513611614},
        {"word":"novo","freq":17.24137931034483},
        {"word":"recurso","freq":17.24137931034483},
        {"word":"justiça segurança","freq":17.05989110707804},
        {"word":"presidente","freq":16.878402903811253},
        {"word":"caso","freq":16.696914700544465},
        {"word":"ser","freq":16.696914700544465},
        {"word":"lava jato","freq":16.696914700544465},
        {"word":"supremo tribunal","freq":16.696914700544465},
        {"word":"tribunal federal","freq":16.696914700544465},
        {"word":"brasília","freq":16.515426497277677},
        {"word":"secretário","freq":16.515426497277677},
        {"word":"governo jair","freq":16.515426497277677},
        {"word":"toda","freq":16.33393829401089},
        {"word":"desde","freq":15.970961887477314},
        {"word":"governo federal","freq":15.970961887477314},
        {"word":"segunda feira","freq":15.789473684210526},
        {"word":"henrique mandetta","freq":15.60798548094374},
        {"word":"tereza cristina","freq":15.60798548094374},
        {"word":"ministro marco","freq":15.60798548094374},
        {"word":"antes","freq":15.426497277676951},
        {"word":"sergio moro","freq":15.245009074410163},
        {"word":"secretaria governo","freq":15.245009074410163},
        {"word":"reforma previdência","freq":15.245009074410163},
        {"word":"foto","freq":15.063520871143377},
        {"word":"ter","freq":15.063520871143377},
        {"word":"empresa","freq":15.063520871143377},
        {"word":"civil onyx","freq":15.063520871143377},
        {"word":"luiz henrique","freq":15.063520871143377},
        {"word":"durante","freq":14.882032667876588},
        {"word":"status ministério","freq":14.882032667876588},
        {"word":"importante","freq":14.519056261343014},
        {"word":"medida","freq":14.519056261343014},
        {"word":"menos","freq":14.337568058076226},
        {"word":"congresso","freq":14.156079854809436},
        {"word":"mudança","freq":13.974591651542651},
        {"word":"brasileiro","freq":13.974591651542651},
        {"word":"outra","freq":13.793103448275861},
        {"word":"após","freq":13.793103448275861},
        {"word":"ministério economia","freq":13.793103448275861},
        {"word":"frente","freq":13.611615245009073},
        {"word":"cultura","freq":13.430127041742287},
        {"word":"então","freq":13.430127041742287},
        {"word":"nova","freq":13.430127041742287},
        {"word":"outra parte","freq":13.430127041742287},
        {"word":"políticas públicas","freq":13.430127041742287},
        {"word":"segunda instância","freq":13.430127041742287},
        {"word":"fazer","freq":13.248638838475499},
        {"word":"presidente jair","freq":13.248638838475499},
        {"word":"quinta feira","freq":13.248638838475499},
        {"word":"responsável","freq":13.06715063520871},
        {"word":"porque","freq":13.06715063520871},
        {"word":"santos cruz","freq":12.885662431941924},
        {"word":"família direitos","freq":12.885662431941924},
        {"word":"banco central","freq":12.704174228675136},
        {"word":"lei rouanet","freq":12.704174228675136},
        {"word":"grande","freq":12.522686025408348},
        {"word":"primeiro escalão","freq":12.522686025408348},
        {"word":"proposta","freq":12.341197822141561},
        {"word":"pessoa","freq":12.341197822141561},
        {"word":"encontro","freq":12.341197822141561},
        {"word":"rio janeiro","freq":12.341197822141561},
        {"word":"secretaria","freq":12.159709618874773},
        {"word":"assim","freq":11.978221415607985},
        {"word":"forma","freq":11.978221415607985},
        {"word":"nesta terça","freq":11.978221415607985},
        {"word":"redes sociais","freq":11.796733212341199},
        {"word":"se","freq":11.61524500907441},
        {"word":"relação","freq":11.61524500907441},
        {"word":"exemplo","freq":11.61524500907441},
        {"word":"tema","freq":11.61524500907441},
        {"word":"secretaria geral","freq":11.61524500907441},
        {"word":"boa vista","freq":11.61524500907441},
        {"word":"operação acolhida","freq":11.61524500907441},
        {"word":"ações","freq":11.433756805807622},
        {"word":"onde","freq":11.433756805807622},
        {"word":"terra cidadania","freq":11.433756805807622},
        {"word":"futuros ministros","freq":11.433756805807622},
        {"word":"primeiro","freq":11.252268602540836},
        {"word":"mil","freq":11.252268602540836},
        {"word":"fernando azevedo","freq":11.252268602540836},
        {"word":"mulher família","freq":11.252268602540836},
        {"word":"ideia","freq":11.070780399274046},
        {"word":"órgão","freq":11.070780399274046},
        {"word":"terça feira","freq":11.070780399274046},
        {"word":"apoio","freq":10.88929219600726},
        {"word":"nesta quarta","freq":10.88929219600726},
        {"word":"acordo","freq":10.707803992740473},
        {"word":"próprio","freq":10.707803992740473},
        {"word":"vai ser","freq":10.707803992740473},
        {"word":"feito","freq":10.526315789473683},
        {"word":"advocacia geral","freq":10.526315789473683},
        {"word":"magno malta","freq":10.526315789473683},
        {"word":"cada","freq":10.344827586206897},
        {"word":"maior","freq":10.344827586206897},
        {"word":"chefe casa","freq":10.344827586206897},
        {"word":"ricardo vélez","freq":10.344827586206897},
        {"word":"fim","freq":10.163339382940109},
        {"word":"governo transição","freq":10.163339382940109},
        {"word":"aurélio mello","freq":10.163339382940109},
        {"word":"momento","freq":9.98185117967332},
        {"word":"controladoria geral","freq":9.98185117967332},
        {"word":"federal stf","freq":9.98185117967332},
        {"word":"fez","freq":9.800362976406534},
        {"word":"partir","freq":9.800362976406534},
        {"word":"têm","freq":9.800362976406534},
        {"word":"assunto","freq":9.800362976406534},
        {"word":"população","freq":9.800362976406534},
        {"word":"anunciado","freq":9.618874773139746},
        {"word":"alguma","freq":9.618874773139746},
        {"word":"parte ministério","freq":9.618874773139746},
        {"word":"azevedo silva","freq":9.618874773139746},
        {"word":"sexta feira","freq":9.618874773139746},
        {"word":"venda bebida","freq":9.618874773139746},
        {"word":"indicado","freq":9.43738656987296},
        {"word":"militar","freq":9.43738656987296},
        {"word":"milhões","freq":9.43738656987296},
        {"word":"dezembro","freq":9.43738656987296},
        {"word":"caminhoneiro","freq":9.43738656987296},
        {"word":"moro justiça","freq":9.43738656987296},
        {"word":"nesta segunda","freq":9.43738656987296},
        {"word":"minas energia","freq":9.43738656987296},
        {"word":"vamos","freq":9.25589836660617},
        {"word":"início","freq":9.25589836660617},
        {"word":"discurso","freq":9.25589836660617},
        {"word":"twitter","freq":9.25589836660617},
        {"word":"bilhões","freq":9.25589836660617},
        {"word":"agência brasil","freq":9.25589836660617},
        {"word":"novo ministro","freq":9.25589836660617},
        {"word":"câmara deputado","freq":9.25589836660617},
        {"word":"qualquer","freq":9.074410163339383},
        {"word":"nada","freq":9.074410163339383},
        ]


def get_categoria_timeline(articles, dias_anteriores):
    date_now = datetime.datetime.now().date()
    
    temp = 0
    timeline_labels, timeline_data = [], []
    for _ in range(dias_anteriores, -1, -1):
        difference = datetime.timedelta(days=-temp)
        requested_date = date_now + difference
        timeline_labels.append(requested_date.strftime("%d-%m-%Y"))
        timeline_data.append(len(articles.filter(Q(date=requested_date))))
        temp += 1
        
    timeline_labels.reverse(), timeline_data.reverse()
    return timeline_labels, timeline_data


def get_relacionamento_categorias(articles, requested_categories):
    nb_noticias = float(len(articles))
    keys = [cat.slug for cat in Category.objects.all()]
    values = np.zeros(len(keys))
    related_cats = dict(zip(keys,values))
    
    for article in articles:
        temp = [category.slug for category in article.categories.all()]
        for cat in temp:
            related_cats[cat] += 1
    
    # ordenando
    related_cats = OrderedDict(sorted(related_cats.items(), key = itemgetter(1), reverse = True))
    
    for key, value in related_cats.items():
        valor = ((value/nb_noticias) * 100)
        str_valor = "%.2f" % valor
        related_cats[key] = str_valor
      
    # removendo do dict a categoria passada nos parametros
    for cat in requested_categories:
        related_cats.pop(cat)
  
    return list(related_cats.keys()), list(related_cats.values())

def paginator(request, article_list):
    #pagination
    page = request.GET.get('page', 1)
 
    paginator = Paginator(article_list, 10)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return articles

def articles_per_region(articles):
    norte = articles.filter(Q(categories=2) | Q(categories=4) | Q(categories=5) | Q(categories=15) | 
                                Q(categories=23) | Q(categories=24) | Q(categories=28)).distinct()
    nordeste = articles.filter(Q(categories=3) | Q(categories=6) | Q(categories=7) | Q(categories=11) | 
                                Q(categories=16) | Q(categories=18) | Q(categories=19) | Q(categories=21) | 
                                Q(categories=27)).distinct()
    centro_oeste = articles.filter(Q(categories=8) | Q(categories=10) | Q(categories=12) | Q(categories=13)).distinct()
    sudeste = articles.filter(Q(categories=9) | Q(categories=14) | Q(categories=20) | Q(categories=26)).distinct()
    sul = articles.filter(Q(categories=17) | Q(categories=22) | Q(categories=25)).distinct()
    
    return norte, nordeste, centro_oeste, sudeste, sul

from functools import wraps

def close_db_connection(ExceptionToCheck=Exception, raise_exception=False, notify=False):
    """Close the database connection when we're finished, django will have to get a new one..."""
    def deco_wrap(f):
        @wraps(f)
        def f_wrap(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                raise e
            finally:
                from django.db import connection; 
                connection.close();

        return f_wrap
    return deco_wrap

# Create your views here.
@close_db_connection()
def category_detail(request, slug):
#     django.db.connections.close_all()
    requested_categories = []
    slugs = slug.split('-and-')
    article_list = Article.objects.all()
    for i in range(len(slugs)): 
        category = Category.objects.get(slug=slugs[i])
        requested_categories.append(category)
        article_list = article_list.filter(categories=category.id).order_by('-date')
    
    norte, nordeste, centro_oeste, sudeste, sul = articles_per_region(article_list)
    labels_region = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'] 
    data_region = [len(norte), len(nordeste), len(centro_oeste), len(sudeste), len(sul)]
    
    articles = paginator(request, article_list)
    
    articles_norte = paginator(request, norte)
    articles_nordeste = paginator(request, nordeste)
    articles_centro_oeste = paginator(request, centro_oeste)
    articles_sudeste = paginator(request, sudeste)
    articles_sul = paginator(request, sul)
    
    labels_category_relation, data_category_relation= get_relacionamento_categorias(articles=article_list, requested_categories=slugs)
    timeline_labels, timeline_data = get_categoria_timeline(articles=article_list, dias_anteriores=30)
    
    print(' --- TITULO ---')
    titles = [cat.title for cat in requested_categories]
    for i in range(len(titles)):
        if(i==0):
            titulo = requested_categories[i].title
        else:
            novo_nome = ' e ' + requested_categories[i].title
            titulo += novo_nome
    
#     dias_anteriores = 30
#     cat = requested_categories[0]
#     print(len(cat.article_set.all()))
#     
#     print(' ---    ----')
#     print(cat.article_set.all()[0])
#     
#     print(' ---  ----')
#     temp = article_list.filter(Q(categories=2), Q(categories=29))
#     print(len(temp))
    
#     Poll.objects.get(
#     Q(question__startswith='Who'),
#     Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
#     )   
    
#     labels_category_timeline, data_category_timeline = analises.get_categoria_timeline(categorias, dias_anteriores)
#     labels_category_relation, data_category_relation = analises.get_relacionamento_categorias(categorias)
#     labels_category_sites, data_category_sites = analises.get_fontes_informacao_categoria(categorias)
#     labels_region, data_region = analises.get_numero_noticias_por_regiao(categorias)
    
    return render(request, 'categories/category_detail.html', 
                  {'categories': requested_categories, 'word_cloud': word_cloud, 
                   'labels_category_timeline': timeline_labels, 'data_category_timeline': timeline_data, 
                   'labels_category_relation': labels_category_relation, 'data_category_relation': data_category_relation,
                   'labels_category_sites': "", 'data_category_sites': "",
                   'labels_region': labels_region, 'data_region': data_region,
                   'articles': articles, 'titulo': titulo,
                   'norte': articles_norte, 'nordeste': articles_nordeste, 'centro_oeste': articles_centro_oeste, 'sudeste': articles_sudeste, 'sul': articles_sul})
    
def category_filter(request):
    if request.method == 'POST':
        form = forms.MultipleChoiceForm(request.POST)
        if form.is_valid():
            # picked = slug das escolhas selecionadas
            categorias = form.cleaned_data.get('categorias')
            
            params = ''
            for i in range(len(categorias)):
                if(i==0):
                    params = categorias[i]
                else:
                    novo_slug = '-and-' + categorias[i] 
                    params = params + novo_slug
            print(params)
        return redirect(reverse('categories:detail', args = (params,)))    
    else:
        form = forms.MultipleChoiceForm()
    return render(request, 'categories/category_filter.html', {'form': form})
#     return render_to_response('categories/category_filter.html', {'form':form },
#         context_instance=RequestContext(request))

@close_db_connection()
@background(schedule=10)
def update_new_category_task(id_category):
    category = Category.objects.get(id=id_category)
    for i in range(1, 1000):
        article_list = Article.objects.all().order_by('-date')[(i-1)*100:i*100]
        if(len(article_list) == 0):
            break
        for article in article_list:   
            categories = pessoas_lexical.django_new_category_lexical_corpus_and_title(article.title, article.body, category)
            if (categories != [set()]):
                all_categorias = Category.objects.all()
                index_categories = util.django_get_categories_idx(categories[0], all_categorias)
                
                for cat_idx in index_categories:
                    article.categories.add(cat_idx)
                
@login_required(login_url="/accounts/login/")
def category_create(request):
    if(request.method == "POST"):
        form = forms.CreateCategory(request.POST)
        if(form.is_valid()):
#            process = subprocess.Popen(['python3', 'manage.py','process_tasks'])
            process = subprocess.Popen(['python', 'manage.py','process_tasks'])
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            
            update_new_category_task(instance.id)
            return redirect('categories:filter')
    else:
        form = forms.CreateCategory()
    return render(request, 'categories/category_create.html', {'form': form})

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer 
