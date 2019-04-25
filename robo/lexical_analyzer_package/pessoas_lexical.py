#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../../../blog')

from robo.lexical_analyzer_package import base_lexical_analyzer

import nltk

# import pandas as pd
# import string 
# import numpy as np

# stemmer = nltk.stem.RSLPStemmer()
# stemmer.stem("copiar")

# categories related to the main theme: security in this case
WORDS = ['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'sergio moro', 'hamilton mourão',
         'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina',
         'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 
         'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 
         'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 
         'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno']


THEME_CATEGORIES = ['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'sérgio moro', 'hamilton mourão',
                     'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina',
                     'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 
                     'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 
                     'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 
                     'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno']

def lexical(df):
    df, categories = base_lexical_analyzer.get_categories_corpus(df, WORDS, THEME_CATEGORIES)
    return df, categories
 
def lexical_corpus_and_title(df):
    df, categories = base_lexical_analyzer.get_categories_corpus_and_title(df, WORDS, THEME_CATEGORIES)
    return df, categories

