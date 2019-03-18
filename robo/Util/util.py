# coding: utf-8

import sys
from numpy import nan
sys.path.insert(0, '../../src')

import requests
import string 

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
