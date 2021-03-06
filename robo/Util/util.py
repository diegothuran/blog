#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib3
import tldextract
import os
import wget
import requests
import shutil
import re

import sys
from numpy import nan
import string 

from slugify import slugify
import json

sys.path.insert(0, '../../../blog')


def remove_punctuation(input_text):
    """
    Removes the punctuation from the input_text string
    python 2 (string.maketrans) is different from python 3 (str.maketrans)
    
    Parameters
    ----------
    input_text: string in which the punctuation will be removed
    
    Return
    ------
        input_text without the puncutation
    """
    punct = string.punctuation
    trantab = str.maketrans(punct, len(punct) * ' ')  # Every punctuation symbol will be replaced by a space
    return input_text.translate(trantab)

def join_strings(list_of_strings):
    """
        Método para transformar tokens em uma única sentença
    :param list_of_strings: Lista com os tokens
    :return: sentença formada pela união dos tokens
    """
    return ", ".join(list_of_strings)

def get_categories_idx(categories_names, index_categories):
    """
    Get the wordpress categories index from the list of strings
    
    Parameters
    ----------
    categories_names: list of strings containing the name of the categories
    
    Return:
    ------
        categories_idx: list of integers containing the index of the categories
    """
#     categories_noticias = df['categorias'].values.tolist()
    list_categories = list(categories_names)
    categories_idx = []
    for category in list_categories:
        category = remove_punctuation(category)
        if category in index_categories.keys():
            categories_idx.append(index_categories[category])
    return categories_idx  

def django_get_categories_idx(categories_names, all_categories):
    """
    Get the wordpress categories index from the list of strings
    
    Parameters
    ----------
    categories_names: list of strings containing the name of the categories
    
    Return:
    ------
        categories_idx: list of integers containing the index of the categories
    """
    list_categories = list(categories_names)
    categories_idx = []
    for category in list_categories:
        for django_category in all_categories:
            if(category == django_category.slug):
                categories_idx.append(django_category.id)
                break
    return categories_idx  

# def get_categories_idx_rest(categories_names, categorias):
#     """
#     Get the wordpress categories index from the list of strings
#     
#     Parameters
#     ----------
#     categories_names: list of strings containing the name of the categories
#     
#     Return:
#     ------
#         categories_idx: list of integers containing the index of the categories
#     """
#     list_categories = list(categories_names)
#     categories_idx = []
#     for category in list_categories:
#         for rest_category in categorias:
#             print(rest_category.slug)
#             if(category == rest_category['slug']):
#                 categories_idx.append(rest_category['id'])
#                 break
#     return categories_idx  

def get_categories_all_noticias(df):
    """
    Get the list of categories (list of categories (str)) for all 'noticias' 
    
    Parameters
    ----------
    df : dataframe containing all the data
    
    Return:
    ------
        list_categorias: list of list of categories for all 'noticias'
    """
    categories_noticias = df['categorias']
    list_categories = []
    for categories_noticia in categories_noticias:
        list_categories.append(remove_punctuation(categories_noticia).split())
    return list_categories

def get_categorias_noticia(df, idx_noticia):
    """
    Get the categories (list of categories (str)) for 'noticia' at idx_noticia index 
    
    Parameters
    ----------
    df : dataframe containing all the data
    
    Return:
    ------
        list_categorias: lista de categorias para a noticia no indice idx_noticia
    """
    categories_noticias = df['categorias']
    list_categories = remove_punctuation(categories_noticias[idx_noticia]).split()
    return list_categories  

def get_reduced_news(news_text):
    """
    Get the reduced text (content) of the news in the in the POST format
    
    Parameters
    ----------
    news_text : initial text of the news (in the current format is the abstract text)
    
    Return:
    ------
        reduced_news: reduced text (content) of the news in the in the POST format
    """
    # get paragraph_tag
    paragraph_tag = '\n'
    tag_idxs = []
    for i, _ in enumerate(news_text):
        if news_text[i:i + len(paragraph_tag)] == paragraph_tag:
            tag_idxs.append(i)
            
    br_tag = '<br />'
    br_idxs = []
    for i, _ in enumerate(news_text):
        if news_text[i:i + len(br_tag)] == br_tag:
            br_idxs.append(i)
            
    img_tag = 'img'
    foto_tag = 'foto'
    globo_tag = 'globo'
    estadao_tag = 'estadão'
    g1_tag = 'g1'
    
    # No caso das noticias do globo    
    try:
        # No caso de as noticias nao virem com imagens
        if(img_tag not in news_text[:tag_idxs[0]]):
            reduced_size = int(len(news_text) / 5)
            reduced_news = news_text[:reduced_size]
        else:
#             # vai comecar a ver a partir da tag final da imagem
            index_after_img = (br_idxs[0] + len(br_tag))
            verification_text = news_text[index_after_img:tag_idxs[5]]
            
            if((globo_tag in verification_text.lower()) or (foto_tag in verification_text.lower()) 
               or (estadao_tag in verification_text.lower()) or (g1_tag in verification_text.lower())):
                paragraph_idx = 0
                for i in range(5, 0, -1):
                    temp = news_text[tag_idxs[i-1]:tag_idxs[i]]
                    if((globo_tag in temp.lower()) or (foto_tag in temp.lower())
                       or (estadao_tag in temp.lower()) or (g1_tag in temp.lower())):
                        paragraph_idx = i
                        break
                    
                # paragrafo vazio
                if(abs(tag_idxs[paragraph_idx + 1] - tag_idxs[paragraph_idx]) < 10):
                    paragraph_idx += 1
                main_content = news_text[tag_idxs[paragraph_idx]:]
                reduced_size = int(len(main_content) / 5)
                reduced_news = main_content[:reduced_size]
            else:
                reduced_size = int(len(verification_text) / 5)
                reduced_news = verification_text[:reduced_size]
    # No caso das noticias do jornal do comercio, que tem um abstract diferente do texto em si
    except:
        reduced_news = news_text

    # Remover '\n' duplicado
    # ver isso no linux: se no lugar do \r\n vai ser so \n (https://stackoverflow.com/questions/14606799/what-does-r-do-in-the-following-script)
    # Tem que deixar essa parte se nao o texto ser postado quebrado
    reduced_news = reduced_news.replace('\n\n\t \n\n', '<p>')
    reduced_news = reduced_news.replace('\n', '<p>')
    
    return reduced_news

def get_reduced_news_with_relevance(news_text, nome_site):
    reduced_news = get_reduced_news(news_text)
    posicionamento_relevancia = get_posicionamento_relevancia(nome_site)
        
#     posicionamento_relevancia = '<div style="float: right;"> \
#     <div style="padding: 8px 8px; background: #81c483; color: #fff; font-weight: 700; border-radius: 4px 4px 0 0;"> RELEVÂNCIA </div>\
#     <div id="relevancia" align="center" style="width:129px; border: 1px solid #81c483"> %s </div>\
#     </div>' % (texto_relevancia,)
    reduced_news = posicionamento_relevancia + reduced_news

    return reduced_news

def get_posicionamento_relevancia(nome_site):
    posicionamento = '<style>\n\
        .relevancia_box .tooltip_relevancia {\n\
        visibility: hidden;\n\
        width: 300px;\n\
        background-color: #555;\n\
        color: #fff;\n\
        text-align: center;\n\
        border-radius: 6px;\n\
        padding: 5px 0;\n\
        position: absolute;\n\
        z-index: 1;\n\
        bottom: 101%%;\n\
        left: 69%%;\n\
        opacity: 0;\n\
        transition: opacity 0.3s\n\
    }\n\
    .relevancia_box .tooltip_relevancia::after {\n\
        content: "";\n\
        position: absolute;\n\
        top: 100%%;\n\
        left: 50%%;\n\
        margin-left: -5px;\n\
        border-width: 5px;\n\
        border-style: solid;\n\
        border-color: #555 transparent transparent transparent\n\
    }\n\
    .relevancia_box:hover .tooltip_relevancia {\n\
        visibility: visible;\n\
        opacity: 1\n\
    }\n\
    </style>\n\
    <div class="relevancia_box" style = "float: right;">\n\
    <div class="tooltip_relevancia">\n\
        Nosso índice de relevância representa uma média da popularidade do site fonte da notícia acessada e é definido pelo Rank Alexa. Na prática, quanto mais próximo de 10.00 for a relevância, maior o número de usuários que visitaram o site fonte dessa notícia. Valores próximo a 0.00 representam um menor o número de acessos à informação.</div>\n\
        <div style="padding: 8px 8px; background: #81c483; color: #fff; font-weight: 700; border-radius: 4px 4px 0 0;"> RELEVÂNCIA </div>\n\
        <div id="relevancia" align="center" style="width:129px; border: 1px solid #81c483"></div>\n\
        </div>\n\
        <script type="text/javascript">\n\
            const http = new XMLHttpRequest()\n\
            site = "%s"\n\
            http.open("GET", "http://34.234.188.90:5000/relevancia/?site=" + site)\n\
            http.send()\n\
            http.onload = () => document.getElementById("relevancia").innerHTML = http.responseText;\n\
        </script>' % (nome_site,) 
    
#     #TODO: COLOCAR O IF NO JAVASCRIPT
#     if(relevancia == 'nan'):
#         texto_relevancia = '-'
#     else:
#         texto_relevancia = relevancia
    
    return posicionamento


def get_sharedcount_info(tracked_url):
    URL = 'https://api.sharedcount.com/v1.0/'
    api_key = '8a2cccc01f801d984aa5995bc3d3594bed656a51'
      
    try:
        payload = {'apikey': api_key, 'url': tracked_url}
        r = requests.get(URL, params=payload)
        info = r.json()

        # Facebook info
        fb_comment = info['Facebook']['comment_count'] + info['Facebook']['comment_plugin_count']
        fb_share = info['Facebook']['share_count']
        fb_reaction = info['Facebook']['reaction_count']
        fb_total = info['Facebook']['total_count']

        return fb_comment, fb_share, fb_reaction, fb_total
    except:
        return 0, 0, 0, 0



def download_image(url, path_to_save_image):
    http = urllib3.PoolManager()
    r = http.request('GET', url, preload_content=False)

    with open(path_to_save_image, 'wb') as out:
        while True:
            data = r.read(15)
            if not data:
                break
            out.write(data)

    r.release_conn()

def extract_domain(link):
    ext = tldextract.extract(link)
    return ext.domain

def download_and_move_image(path_to_image):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root_path = root_path.replace('/robo', '/media')
    try:
        file_name = wget.download(path_to_image)
        print(file_name)
        dst = os.path.join(root_path, 'images', file_name)
        print(dst)
        shutil.move(os.path.join(os.getcwd(), file_name), dst)
        dst = '/media/images/' + file_name
    except Exception as e:
        print(e)
        dst = '0'
    return dst

def clean_join_strings(list_of_strings):
    """
        Método para transformar tokens em uma única sentença
    :param list_of_strings: Lista com os tokens
    :return: sentença formada pela união dos tokens
    """
    return "".join(list_of_strings)


def join_categories(categories):
    str_categories = ', '.join(str(c) for c in categories)
    return str_categories

def categories_db_to_categories(categories_db):
    categories = categories_db.split(', ')
    return categories

def slugify_title(title):
    slug = slugify(title)
    return slug

def get_json_categories():
    categorias = requests.request("GET", 'http://127.0.0.1:8000/categorias/listar/')
    json_categories = json.loads(categorias.content)
    return json_categories

# def categoria_to_sigla(requested_categories):
#     categorias = [ 'Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 
#                   'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 
#                   'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 
#                   'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
#     
#     siglas = ['ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa','pb', 'pr', 
#                   'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se','to']
#     retorno = []
#     for cat in requested_categories:
#         idx = categorias.index(cat)
#         retorno.append(siglas[idx])
#     return retorno
# 
# # categoria_to_sigla('Acre')


# def categoria_to_sigla(requested_categories):
#     '''
#     chamado no categories.views 
#     '''
#     categorias = [ 'Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 
#                   'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 
#                   'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 
#                   'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins',
#                   'Bolsonaro', 'Onyx Lorenzoni',  'Paulo Guedes',  'Augusto Heleno',  'Marcos Pontes',  'Sérgio Moro', 
#                   'Hamilton Mourão', 'Joaquim Levy', 'Mansueto almeida', 'Fernando Azevedo e Silva', 'Ernesto Araújo',  
#                   'Roberto Campos Neto', 'Tereza Cristina', 'André Luiz de Almeida Mendonça', 'Carlos Von Doellinger', 
#                   'Érika Marena', 'Luiz Mandetta', 'Maurício Valeixo', 'Pedro Guimarães', 'Ricardo Vélez Rodríguez', 
#                   'Roberto Castello Branco', 'Rubem Novaes', 'Wagner Rosário', 'Bento Costa Lima Leite de Albuquerque Junior', 
#                   'Marcelo Álvaro Antônio', 'Osmar Terra', 'Gustavo Henrique Rigodanzo Canuto', 'Tarcísio Gomes de Freitas', 
#                   'Carlos Alberto dos Santos Cruz', 'Gustavo Bebianno']
#     
#     siglas = ['ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa','pb', 'pr', 
#                   'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se','to',
#                   'bolsonaro', 'onyx lorenzoni',  'paulo guedes',  'augusto heleno',  'marcos pontes',  'sérgio moro', 
#                   'hamilton mourão', 'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo',  
#                   'roberto campos neto', 'tereza cristina', 'andré luiz de almeida mendonça', 'carlos von doellinger', 
#                   'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 'ricardo vélez rodríguez', 
#                   'roberto castello branco', 'rubem novaes', 'wagner rosário', 'bento costa lima leite de albuquerque junior', 
#                   'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 'tarcísio gomes de freitas', 
#                   'carlos alberto dos santos cruz', 'gustavo bebianno']
#     
#     retorno = []
#     for i in range(len(requested_categories)):
#         idx = categorias.index(requested_categories[i].title)
#         retorno.append(siglas[idx])
#         if(i==0):
#             titulo = requested_categories[i].title
#         else:
#             novo_nome = ' e ' + requested_categories[i].title
#             titulo += novo_nome
#     return retorno, titulo
# 
# def sigla_to_categoria(siglas_categorias):
#     '''
#     chamado no categories.views 
#     '''
#     categorias = [ 'Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 
#                   'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 
#                   'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 
#                   'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins',
#                   'Bolsonaro', 'Onyx Lorenzoni',  'Paulo Guedes',  'Augusto Heleno',  'Marcos Pontes',  'Sérgio Moro', 
#                   'Hamilton Mourão', 'Joaquim Levy', 'Mansueto almeida', 'Fernando Azevedo e Silva', 'Ernesto Araújo',  
#                   'Roberto Campos Neto', 'Tereza Cristina', 'André Luiz de Almeida Mendonça', 'Carlos Von Doellinger', 
#                   'Érika Marena', 'Luiz Mandetta', 'Maurício Valeixo', 'Pedro Guimarães', 'Ricardo Vélez Rodríguez', 
#                   'Roberto Castello Branco', 'Rubem Novaes', 'Wagner Rosário', 'Bento Costa Lima Leite de Albuquerque Junior', 
#                   'Marcelo Álvaro Antônio', 'Osmar Terra', 'Gustavo Henrique Rigodanzo Canuto', 'Tarcísio Gomes de Freitas', 
#                   'Carlos Alberto dos Santos Cruz', 'Gustavo Bebianno']
#     
#     siglas = ['ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa','pb', 'pr', 
#                   'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se','to',
#                   'bolsonaro', 'onyx lorenzoni',  'paulo guedes',  'augusto heleno',  'marcos pontes',  'sérgio moro', 
#                   'hamilton mourão', 'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo',  
#                   'roberto campos neto', 'tereza cristina', 'andré luiz de almeida mendonça', 'carlos von doellinger', 
#                   'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 'ricardo vélez rodríguez', 
#                   'roberto castello branco', 'rubem novaes', 'wagner rosário', 'bento costa lima leite de albuquerque junior', 
#                   'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 'tarcísio gomes de freitas', 
#                   'carlos alberto dos santos cruz', 'gustavo bebianno']
#     
#     retorno = []
#     for i in range(len(siglas_categorias)):
#         idx = siglas.index(siglas_categorias[i])
#         retorno.append(categorias[idx])
#     return retorno
    