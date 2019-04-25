#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../../blog')

from robo.Model import News
from robo.Database import connection, relevancia_site_table
import datetime
from dateutil import parser
# import postagem.Util as Util
from robo.Model.Relevancia_Site import Relevancia_Site 
from operator import itemgetter    

from collections import OrderedDict

from robo.pages.util import load_pages
import wordcloud
import nltk

INDEX_REGIOES = { 'Norte' : 0,
                    'Nordeste' : 0,
                    'Centro-Oeste' : 0,
                    'Sudeste' : 0,
                    'Sul' : 0}

INDEX_CATEGORIES = {
#     'categoria': '',
                    'bolsonaro' : 0,
                    'onyx lorenzoni' : 0, 
                    'paulo guedes' : 0, 
                    'augusto heleno' : 0, 
                    'marcos pontes' : 0, 
                    'sérgio moro' : 0,
                    'hamilton mourão' : 0,
                    'joaquim levy' : 0,
                    'mansueto almeida' : 0,
                    'fernando azevedo e silva' : 0,
                    'ernesto araújo' : 0, 
                    'roberto campos neto' : 0,
                    'tereza cristina' : 0,
                    'andré luiz de almeida mendonça' : 0,
                    'carlos von doellinger' : 0,
                    'érika marena' : 0,
                    'luiz mandetta' : 0,
                    'maurício valeixo' : 0,
                    'pedro guimarães' : 0,
                    'ricardo vélez rodríguez' : 0,
                    'roberto castello branco' : 0,
                    'rubem novaes' : 0,
                    'wagner rosário' : 0,
                    'bento costa lima leite de albuquerque junior' : 0, 
                    'marcelo álvaro antônio' : 0, 
                    'osmar terra' : 0, 
                    'gustavo henrique rigodanzo canuto' : 0, 
                    'tarcísio gomes de freitas' : 0, 
                    'carlos alberto dos santos cruz' : 0, 
                    'gustavo bebianno' : 0,
 
#                     'jungmann' : 0, 
#                     'haddad' : 0, 
                    'ac' : 0,
                    'al' : 0,
                    'ap' : 0,
                    'am' : 0,
                    'ba' : 0,
                    'ce' : 0,
                    'df' : 0,
                    'es' : 0,
                    'go' : 0,
                    'ma' : 0,
                    'mt' : 0,
                    'ms' : 0,
                    'mg' : 0,
                    'pa' : 0,
                    'pb' : 0,
                    'pr' : 0,
                    'pe' : 0,
                    'pi' : 0,
                    'rj' : 0,
                    'rn' : 0,
                    'rs' : 0,
                    'ro' : 0,
                    'rr' : 0,
                    'sc' : 0,
                    'sp' : 0,
                    'se' : 0,
                    'to' : 0
                    }

def get_relacionamento_categorias(categorias):
    # cats = todas as categorias das noticias que tem que a(s) categoria(s) do parametro
    cats = relevancia_site_table.select_categories(categorias)
    nb_noticias = len(cats)
    related_cats = INDEX_CATEGORIES.copy()
    for row in cats:
        categories_per_row = row[0]
        try:
            if(',' in categories_per_row):
                categories = categories_per_row.split(', ')
                for category in categories:
                    related_cats[category] += 1
            else: # only one category in the table
                related_cats[categories_per_row] += 1
        except:
            pass
    
    # ordenando
    related_cats = OrderedDict(sorted(related_cats.items(), key = itemgetter(1), reverse = True)) 

    for key, value in related_cats.items():
        valor = ((value/nb_noticias) * 100)
        str_valor = "%.2f" % valor
        related_cats[key] = str_valor
    
    # removendo do dict a categoria passada nos parametros
    for cat in categorias:
        related_cats.pop(cat)

    return list(related_cats.keys()), list(related_cats.values())

# get_relacionamento_categorias(['osmar terra', 'rs', 'ms'])
# get_relacionamento_categorias(['osmar terra'])

def get_fontes_informacao_categoria(categorias):
    sites = {}
    for page in load_pages.PAGES:
        sites[page.NAME] = 0

    fontes_informacao = relevancia_site_table.select_news_source_categories(categorias)
    todos_sites = sites.copy()
    for fonte in fontes_informacao:
        try:
            #fonte vem no formato de tupla por isso fonte[0]
            todos_sites[fonte[0]] += 1
        except:
            pass
    
    # tirando o rss_multiplos para nao aparecer no grafico
    todos_sites.pop('rss_multiplos')
    # tirando sites que tem valor 0
    todos_sites = {x:y for x,y in todos_sites.items() if y!=0}
    # ordenando
    ordenado = OrderedDict(sorted(todos_sites.items(), key = itemgetter(1), reverse = True)) 
          
    return list(ordenado.keys()), list(ordenado.values())

# get_fontes_informacao_categoria(['osmar terra'])

def get_categoria_timeline(categorias, dias_anteriores):
    date_now = datetime.datetime.now()   
#     str_now = date_now.strftime('%Y-%m-%d %H:%M:%S')
    str_now = date_now.strftime('%Y-%m-%d')
#     dias_anteriores = 30
    datas = []
    datas.append(str_now)
    temp = 1
    for i in range(dias_anteriores, 0, -1):
        difference = datetime.timedelta(days=-temp)
        data = date_now + difference
        datas.append(data.strftime('%Y-%m-%d'))
        temp += 1
    datas.reverse()
    # consulta ao banco
    datas_categoria = relevancia_site_table.get_interval_category(categorias, datas[0], datas[-1])
    # criando o dict
    dict_datas = { i : 0 for i in datas}
    # preenchendo o dict 
    for data in datas_categoria:
        categoria_por_data = data[0].strftime('%Y-%m-%d')
        try:
            dict_datas[categoria_por_data] += 1
        except:
            pass
    # formatando o dict
    datas_formatadas = {}
    for element in dict_datas:
        new_fmt = datetime.datetime.strptime(element, '%Y-%m-%d').strftime("%d-%m-%Y")
        datas_formatadas[new_fmt] = dict_datas[element]
    
#     print(dict_datas) 
#     print(datas_formatadas) 
#     print(datas_formatadas.keys())
#     print(datas_formatadas.values())
    
    return list(datas_formatadas.keys()), list(datas_formatadas.values())

# get_categoria_timeline(['osmar terra', 'rs'], 30)

def get_timeline(dias_anteriores):
    date_now = datetime.datetime.now()   
#     str_now = date_now.strftime('%Y-%m-%d %H:%M:%S')
    str_now = date_now.strftime('%Y-%m-%d')
#     dias_anteriores = 30
    datas = []
    datas.append(str_now)
    temp = 1
    for i in range(dias_anteriores, 0, -1):
        difference = datetime.timedelta(days=-temp)
        data = date_now + difference
        datas.append(data.strftime('%Y-%m-%d'))
        temp += 1
    datas.reverse()
    # consulta ao banco
    datas_categoria = relevancia_site_table.get_interval(datas[0], datas[-1])
    # criando o dict
    dict_datas = { i : 0 for i in datas}
    # preenchendo o dict 
    for data in datas_categoria:
        categoria_por_data = data[0].strftime('%Y-%m-%d')
        try:
            dict_datas[categoria_por_data] += 1
        except:
            pass
    # formatando o dict
    datas_formatadas = {}
    for element in dict_datas:
        new_fmt = datetime.datetime.strptime(element, '%Y-%m-%d').strftime("%d-%m-%Y")
        datas_formatadas[new_fmt] = dict_datas[element]
    
    print(dict_datas) 
    print(datas_formatadas) 
    print(datas_formatadas.keys())
    print(datas_formatadas.values())
    
    soma = 0
    for i in datas_formatadas.values():
        soma += i
        print(soma)
    
    print('soma final')
    print(soma)


def get_numero_noticias_por_regiao(categorias):                
    # cats = todas as categorias das noticias que tem que a(s) categoria(s) do parametro
    cats = relevancia_site_table.select_categories(categorias)
    related_cats = INDEX_REGIOES.copy()
    for row in cats:
        categories_per_row = row[0]
        try:
            if(',' in categories_per_row):
                categories = categories_per_row.split(', ')
                norte, nordeste, centro, sudeste, sul = True, True, True, True, True
                for category in categories:
                    if(category in ['ac', 'ap', 'am', 'pa', 'ro', 'rr', 'to']):
                        if(norte):
                            related_cats['Norte'] += 1
                            norte = False
                    if(category in ['al', 'ba', 'ce', 'ma', 'pb', 'pe', 'pi', 'rn', 'se']):
                        if(nordeste):
                            related_cats['Nordeste'] += 1
                            nordeste = False
                    if(category in ['df', 'go', 'mt', 'ms']):
                        if(centro):
                            related_cats['Centro-Oeste'] += 1
                            centro = False
                    if(category in ['es', 'mg', 'rj', 'sp']):
                        if(sudeste):
                            related_cats['Sudeste'] += 1
                            sudeste = False
                    if(category in ['pr', 'rs', 'sc']):
                        if(sul):
                            related_cats['Sul'] += 1
                            sul = False
                            
            else: # only one category in the table
                related_cats[categories_per_row] += 1
        except:
            pass
    
    return list(related_cats.keys()), list(related_cats.values())

# get_numero_noticias_por_regiao(['ba'])

def categorias_por_site(site):
    categorias = relevancia_site_table.get_categories_per_site(site)
    cats_counter = INDEX_CATEGORIES.copy()
    for row in categorias:
        categories_per_row = row[0]
        try:
            if(',' in categories_per_row):
                categories = categories_per_row.split(', ')
                for category in categories:
                    cats_counter[category] += 1
            else: # only one category in the table
                cats_counter[categories_per_row] += 1
        except:
            pass
    print(cats_counter)
    print(cats_counter.keys())
    print(cats_counter.values())

# def get_relevancia(site):
#     # estrutura tupla = (id, site, relevancia, relevancia_inicial)
#     tupla = relevancia_site_table.select(site)
#     relevancia = tupla[2]
#     return relevancia

def get_relevancia(link):
    site = relevancia_site_table.select_site_in_link(link)[0]
    # estrutura tupla = (id, site, relevancia, relevancia_inicial)
    tupla = relevancia_site_table.select(site[0])
    relevancia = tupla[2]
    return relevancia

# link = 'https://noticias.uol.com.br/ultimas-noticias/agencia-estado/2019/04/01/desgaste-do-governo-nao-interessa-a-ninguem-diz-governador-da-bahia.htm'
# get_relevancia(link)

def get_wordcloud(categoria):
#     categoria = 'osmar terra'
    noticias = relevancia_site_table.select_text_categories(categoria)
    news = [noticia[0] for noticia in noticias]
    # Create and generate a word cloud image:
    temp = ''
    from nltk.tokenize import word_tokenize
    from string import punctuation
    for new in news:
        palavras = word_tokenize(new.lower())
        
        stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))
        palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]
        for palavra in palavras_sem_stopwords:
            temp = temp + ' ' + palavra

    
    wc = wordcloud.WordCloud().generate(temp)
    
    print('[')
    for key, value in wc.words_.items():
#         print('{"word":"' + str(key) + '","freq":' + str(value) + '},')
        valor = value * 100
        print('{"word":"' + str(key) + '","freq":' + str(valor) + '},')
    print(']')
    
#     # Display the generated image:
#     plt.imshow(wc, interpolation='bilinear')
#     plt.axis("off")
#     plt.show()

# site = 'buzzfeed.com'
# # estrutura tupla = (id, site, relevancia, relevancia_inicial)
# tupla = relevancia_site_table.select(site)
# print(tupla[2])


# def plot_bar_timeseries(valores, dates):
#     # this is for plotting purpose
# #     index = np.arange(len(valores))
#     index = []
#     for date in dates:
# #         str_date = date.strftime("%Y-%m-%d")
#         str_date = date.strftime("%d-%m-%Y")
#         index.append(str_date)
#     plt.bar(index, valores)
#     plt.xlabel('Data', fontweight='bold')
#     plt.ylabel('Número de notícias', fontweight='bold')
#     plt.xticks(rotation=30)
#     plt.title('Timeline das notícias')
# #     plt.xlabel('Genre', fontsize=5)
# #     plt.ylabel('No of Movies', fontsize=5)
# #     plt.xticks(index, valores, fontsize=5, rotation=30)
# #     plt.title('Market Share for Each Genre 1995-2017')
#     plt.show()
#       
# # dates = [datetime.date(2018, 11, 1), datetime.date(2018, 11, 2), datetime.date(2018, 11, 3), datetime.date(2018, 11, 4)]
#            
# dates = [datetime.date(2018, 11, 1), datetime.date(2018, 11, 2), datetime.date(2018, 11, 3), datetime.date(2018, 11, 4), 
#          datetime.date(2018, 11, 5), datetime.date(2018, 11, 6), datetime.date(2018, 11, 7), datetime.date(2018, 11, 8),
#          datetime.date(2018, 11, 9), datetime.date(2018, 11, 10), datetime.date(2018, 11, 11), datetime.date(2018, 11, 12), datetime.date(2018, 11, 13)]
#   
# valores = []
# for date in dates:
#     valores.append(relevancia_site_table.select_form_date(date))
#   
# print(valores)
# plot_bar_timeseries(valores, dates)
 
# data_inicial = datetime.date(2018, 11, 1) 
# data_final = datetime.date(2018, 11, 4)
# relevancia_site_table.get_interval(data_inicial, data_final)

# site = 'www.valor.com.br'
# # relevancia_site_table.select_site_in_link(site)
# relevancia_site_table.update_site(site)

''' AQUI '''
# for page in load_pages.PAGES:
#     site = page.NAME
#     print(site)
#     relevancia_site_table.update_site(site)
 
# relevancia_site_table.select_site(site)
# 
# # categories_db = relevancia_site_table.select_site_pd(site)
# # n_news = float(len(categories_db)) 
# # print(categories_db)
# 
# 
# # THEME_CATEGORIES = ['bolsonaro', 'onyx lorenzoni', 'paulo guedes']
# 
# THEME_CATEGORIES = ['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'sérgio moro', 'hamilton mourão',
#                      'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina',
#                      'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 
#                      'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 
#                      'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 
#                      'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno']
# 
# 

# 
# retorno = []
# for theme in THEME_CATEGORIES:
#     row = INDEX_CATEGORIES.copy()
# #     row['categoria'] = theme
#     for categories_per_row in categories_db:
#         if(theme in categories_per_row):
#             if(',' in categories_per_row):
#                 categories = categories_per_row.split(', ')
#                 for category in categories:
#                     row[category] += 1
#             else: # only one category in the table
#                 row[categories_per_row] += 1
#     retorno.append(row)
# 
# print('retorno')
# print(len(retorno))
# df = pd.DataFrame(retorno, index=THEME_CATEGORIES)
# # print(df.loc['bolsonaro'])
# for i in range(len(df)):
#     print(i)
# #     print(df.iloc[i].name)
#     print(df.iloc[i].values)
#     valores = df.iloc[i].values
# #     soma = np.sum(valores)
# #     print(soma)
#     percentagem = None
#     percentagem =  valores/n_news
#     print(percentagem)
# print(df)
# 
# # a = list(retorno[0].values())
# # b = a[1:]
# 
# # print(np.cov(b))
# 
# # print('\n COOR MATRIX')
# # # df['A'].corr(df['B'])
# # # coor_matrix = df.corr()
# # coor_matrix = df.corr()
# # 
# # print(coor_matrix['bolsonaro'])
# # print(len(coor_matrix['bolsonaro']))

''' --- Codigos para o js relacionado a categorias --- '''
# categoria = 'osmar terra'
# dias_anteriores = 30
# get_categoria_timeline(categoria, dias_anteriores)
# get_relacionamento_categorias(categoria)
# get_fontes_informacao_categoria(categoria)
# get_wordcloud(categoria)

''' timeline geral '''
# get_timeline(dias_anteriores)

# ''' --- Codigos para o js relacionado a sites --- '''
# site = 'terra.com.br'
# categorias_por_site(site)