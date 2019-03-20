#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import string 
import numpy as np

# Location categories
ESTADOS = ['alagoas', 'amapá', 'amazonas', 'bahia', 'ceará', 'distrito federal',  'espírito santo',  'goiás',  
           'maranhão', 'mato grosso',  'mato grosso do sul',  'minas gerais',  'paraíba',  'paraná',  'pernambuco',  
           'piauí',  'rio de janeiro', 'rio grande do norte', 'rio grande do sul', 'rondônia', 'roraima', 'santa catarina', 
           'são paulo', 'sergipe', 'tocantins']

ESTADO_PARA = 'Pará'

ESTADO_ACRE = 'Acre' 

CAPITAIS = ['rio branco', 'maceió', 'macapá', 'manaus', 'brasília',  'goiânia', 'são luís',
            'cuiabá', 'campo grande', 'belo horizonte', 'belém', 'joão pessoa', 'curitiba', 'recife', 'teresina', 'rio de janeiro',
            'porto alegre', 'porto velho', 'boa vista', 'florianópolis', 'são paulo', 'aracaju']

CAPITAIS_CASE_SENSITIVE = ['Natal', 'Salvador', 'Fortaleza', 'Vitória', 'Palmas']

SIGLAS_ESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA','PB', 'PR', 
                  'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE','TO']

SIGLAS_ESTADOS_SEM_PA_AC = ['AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PB', 'PR', 
                  'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE','TO']


SIGLAS_ESTADOS_SEM_CASE_SENSITIVE = ['AC', 'AL', 'AP', 'AM', 'DF', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA','PB', 'PR', 
                  'PE', 'PI', 'RJ', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE']  

SIGLAS_ESTADOS_CASE_SENSITIVE = ['RN', 'BA', 'CE', 'ES' , 'TO'] 


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
    trantab = str.maketrans(punct, len(punct)*' ')  # Every punctuation symbol will be replaced by a space
    return input_text.translate(trantab)

def get_estados_categories(input_text):
    """
    input_text: deve estar no formato original, a transformacao para lower vai ser feita durante o metodo
    """
    estados_categories = []
#     try:
    text = remove_punctuation(input_text)

    ' CASE_SENSITIVE VERIFICATION '
    # Seek for SIGLAS_ESTADOS sigla
    words = text.split()
    for word in words:
        if word in SIGLAS_ESTADOS:
            estados_categories.append(word.lower())
        
    for idx_capitais in range(len(CAPITAIS_CASE_SENSITIVE)):
        if CAPITAIS_CASE_SENSITIVE[idx_capitais] in text:
            estados_categories.append(SIGLAS_ESTADOS_CASE_SENSITIVE[idx_capitais].lower())

    # Pará, caso a parte, para evitar o erro de verbo no futuro 'parará'
    if ESTADO_PARA in text:
        estados_categories.append('pa')
    
    # Acre, caso a parte, para evitar o erro de verbo acreditar    
    if ESTADO_ACRE in text:
        estados_categories.append('ac')

    ' LOWER_CASE VERIFICATION: text to lower case '
    text = text.lower()

    # seek for ESTADOS name
    for idx_estado in range(len(ESTADOS)):
        if ESTADOS[idx_estado] in text:
            estados_categories.append(SIGLAS_ESTADOS_SEM_PA_AC[idx_estado].lower())

    # seek for CAPITAIS name
    for idx_capitais in range(len(CAPITAIS)):
        if CAPITAIS[idx_capitais] in text:
            estados_categories.append(SIGLAS_ESTADOS_SEM_CASE_SENSITIVE[idx_capitais].lower())

    return estados_categories


def get_theme_categories(input_text, words, theme_categories, words_case_sensitive=None, theme_categories_case_sensitive=None):
    """
    input_text: deve estar no formato original, a transformacao para lower vai ser feita durante o metodo
    words: palavras da busca
    theme_categories: categorias relacionadas ao tema principal do analisador lexico
    """
    related_categories = []
#     try:
    text = remove_punctuation(input_text)
    
    #Case sensitive
    if(words_case_sensitive is not None):
        splited_text = text.split()                
        for splited in splited_text:
            if splited in words_case_sensitive:
                related_categories.append(splited.lower())
    
    # LOWER_CASE VERIFICATION: text to lower case
    lower_text = text.lower()

    # seek for ESTADOS name
    for idx in range(len(words)):
        if words[idx] in lower_text:
            related_categories.append(theme_categories[idx])
#             related_categories.append(theme_categories[idx].lower())

    return related_categories

def get_categories(input_text, words, theme_categories, words_case_sensitive=None, theme_categories_case_sensitive=None):
    """
    input_text: deve estar no formato original, a transformacao para lower vai ser feita durante o metodo
    theme_categories: categorias relacionadas ao tema principal do analisador lexico
    """
    cats, main_theme_categories, estados_categories = [], [], []
    try:
        main_theme_categories = get_theme_categories(input_text, words, theme_categories, words_case_sensitive, theme_categories_case_sensitive)
        if(main_theme_categories != []):
            estados_categories = get_estados_categories(input_text)

        cats_concat = main_theme_categories + estados_categories
        cats.append(cats_concat)

    except:
        cats.append([])

    return cats

def get_categories_corpus(df, words, theme_categories, words_case_sensitive=None, theme_categories_case_sensitive=None):
    """
    categories from rss: input_text is just from the 'noticias'
    
    Parameters
    ----------
    input_text: deve estar no formato original, a transformacao para lower vai ser feita durante o metodo
    theme_categories: categorias relacionadas ao tema principal do analisador lexico
    
    Return
    ------
    df: the df with the column 'categories'
    set_cats: set of categories
    """
    cats = []
    for idx in range(len(df)):
        row = df.iloc[idx]
        noticia = row['noticia']
        cats = get_categories(noticia, words, theme_categories, words_case_sensitive, theme_categories_case_sensitive)

    # Removing replicated items
    set_cats = [set(cat) for cat in cats]

    df = df.assign(categorias = set_cats)
    return df, set_cats

def get_categories_corpus_and_title(df, words, theme_categories, words_case_sensitive=None, theme_categories_case_sensitive=None):
    """
    categories from corpus and title: input_text is from both 'noticia' and 'titulo' 
    
    Parameters
    ----------
    input_text: deve estar no formato original, a transformacao para lower vai ser feita durante o metodo
    theme_categories: categorias relacionadas ao tema principal do analisador lexico
    
    Return
    ------
    df: the df with the column 'categories'
    set_cats: set of categories
    """
    cats = []
    for idx in range(len(df)):
        row = df.iloc[idx]
        
        noticia = row['noticia']
        cats_noticia = get_categories(noticia, words, theme_categories, words_case_sensitive, theme_categories_case_sensitive)

        title = row['titulos']
        cats_title = get_categories(title, words, theme_categories, words_case_sensitive, theme_categories_case_sensitive)

    cats_concat = cats_noticia[0] + cats_title[0]
    cats.append(cats_concat)

    # Removing replicated items
    set_cats = [set(cat) for cat in cats]
    
    df = df.assign(categorias = set_cats)
    return df, set_cats


# --- Tree Structure ---
def check_string(word, lower_text):
    in_the_text = (word in lower_text)
    return in_the_text

def check_list(list_words, lower_text):
    if(len(list_words) > 1):
        temp2 = []
        for i in range(len(list_words)):
            ablibla = (list_words[i] in lower_text)
            temp2.append(ablibla)
        if(True in temp2):
            in_the_text = True
        else:
            in_the_text = False
    else:
        in_the_text = (list_words[0] in lower_text)

    return in_the_text


def get_theme_categories_tree_structure(input_text, clustered_search_words, theme_categories):
    """
    input_text: deve estar no formato original, a transformacao para lower vai ser feita durante o metodo
    clustered_search_words: as palavras agrupadas no formato dado
    theme_categories: categorias relacionadas ao tema principal do analisador lexico
    """
#     try:
    text = remove_punctuation(input_text)
    
    #TODO: ver se vai precisar fazer case sensitive 
    
    # LOWER_CASE VERIFICATION: text to lower case
    lower_text = text.lower()
    cats = []
    for idx in range(len(clustered_search_words)):
        words_tree = clustered_search_words[idx]
        if(len(words_tree) > 1):
            checker = []
            for i in range(len(words_tree)):
                # Check if the item is a string or a list of strings
                if(type(words_tree[i]) == str):
                    str_in_the_text = check_string(words_tree[i], lower_text)
                    checker.append(str_in_the_text)
                else:
                    list_in_the_text = check_list(words_tree[i], lower_text)
                    checker.append(list_in_the_text)
            if(False not in checker):
                cats.append(theme_categories[idx])
        else:
            if words_tree[0] in lower_text:
                cats.append(theme_categories[idx])

    return cats

def get_categories_tree_structure(input_text, words_tree_structure, theme_categories):
    """
    input_text: deve estar no formato original, a transformacao para lower vai ser feita durante o metodo
    words_tree_structure: words in the tree structure
    theme_categories: categorias relacionadas ao tema principal do analisador lexico
    """
    cats, main_theme_categories, estados_categories = [], [], []
    try:
        main_theme_categories = get_theme_categories_tree_structure(input_text, words_tree_structure, theme_categories)
        if(main_theme_categories != []):
            estados_categories = get_estados_categories(input_text)

        cats_concat = main_theme_categories + estados_categories
        cats.append(cats_concat)

    except:
        cats.append([])

    return cats

def get_categories_corpus_tree_structure(df, words_tree_structure, theme_categories):
    """
    categories from rss: input_text is just from the 'noticias'
    
    Parameters
    ----------
    input_text: deve estar no formato original, a transformacao para lower vai ser feita durante o metodo
    theme_categories: categorias relacionadas ao tema principal do analisador lexico
    
    Return
    ------
    df: the df with the column 'categories'
    set_cats: set of categories
    """
    cats = []
    for idx in range(len(df)):
        row = df.iloc[idx]
        noticia = row['noticia']
        cats = get_categories_tree_structure(noticia, words_tree_structure, theme_categories)

    # Removing replicated items
    set_cats = [set(cat) for cat in cats]

    df = df.assign(categorias = set_cats)
    return df, set_cats

def get_categories_corpus_and_title_tree_structure(df, words_tree_structure, theme_categories):
    """
    categories from corpus and title: input_text is from both 'noticia' and 'titulo' 
    
    Parameters
    ----------
    input_text: deve estar no formato original, a transformacao para lower vai ser feita durante o metodo
    theme_categories: categorias relacionadas ao tema principal do analisador lexico
    
    Return
    ------
    df: the df with the column 'categories'
    set_cats: set of categories
    """
    cats = []
    for idx in range(len(df)):
        row = df.iloc[idx]
        
        noticia = row['noticia']
        cats_noticia = get_categories_tree_structure(noticia, words_tree_structure, theme_categories)

        title = row['titulos']
        cats_title = get_categories_tree_structure(title, words_tree_structure, theme_categories)

    cats_concat = cats_noticia[0] + cats_title[0]
    cats.append(cats_concat)

    # Removing replicated items
    set_cats = [set(cat) for cat in cats]
    
    df = df.assign(categorias = set_cats)
    return df, set_cats

# def lexical(df, theme_categories):
#     df, categories = get_categories_corpus(df, theme_categories)
#     return df, categories
# 
# def lexical_corpus_and_title(df, theme_categories):
#     df, categories = get_categories_corpus_and_title(df, theme_categories)
#     return df, categories
    