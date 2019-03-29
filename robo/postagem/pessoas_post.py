#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
# import base64
import datetime

from robo.Util import util
# from robo.Database import relevancia_site_table

# USER = b'admxarx'
# PASSWORD = b'!xarx@2018*'
# 
# # URL = 'https://seguranca.xarx.rocks/wp-json/wp/v2'
# URL = 'https://varejo.xarx.rocks/wp-json/wp/v2'
# 
# token = base64.standard_b64encode(USER + b':' + PASSWORD)
# headers = {b'Authorization': b'Basic ' + token}

# categoria sem_categoria : 1
INDEX_CATEGORIES = {'ac' : 2,
                    'al' : 3,
                    'ap' : 4,
                    'am' : 5,
                    'ba' : 6,
                    'ce' : 7,
                    'df' : 8,
                    'es' : 9,
                    'go' : 10,
                    'ma' : 11,
                    'mt' : 12,
                    'ms' : 13,
                    'mg' : 14,
                    'pa' : 15,
                    'pb' : 16,
                    'pr' : 17,
                    'pe' : 18,
                    'pi' : 19,
                    'rj' : 20,
                    'rn' : 21,
                    'rs' : 22,
                    'ro' : 23,
                    'rr' : 24,
                    'sc' : 25,
                    'sp' : 26,
                    'se' : 27,
                    'to' : 28,
    
#                     'jungmann' : 8, 
#                     'haddad' : 10, 
                    'bolsonaro' : 29,
                    'onyx lorenzoni' : 30, 
                    'paulo guedes' : 31, 
                    'augusto heleno' : 32, 
                    'marcos pontes' : 33, 
                    'sérgio moro' : 34,
                    'hamilton mourão' : 35,
                    'joaquim levy' : 36,
                    'mansueto almeida' : 37,
                    'fernando azevedo e silva' : 38,
                    'ernesto araújo' : 39, 
                    'roberto campos neto' : 40,
                    'tereza cristina' : 41,
                    'andré luiz de almeida mendonça' : 42,
                    'carlos von doellinger' : 43,
                    'érika marena' : 44,
                    'luiz mandetta' : 45,
                    'maurício valeixo' : 46,
                    'pedro guimarães' : 47,
                    'ricardo vélez rodríguez' : 48,
                    'roberto castello branco' : 49,
                    'rubem novaes' : 50,
                    'wagner rosário' : 51,
                    'bento costa lima leite de albuquerque junior' : 52, 
                    'marcelo álvaro antônio' : 53, 
                    'osmar terra' : 54, 
                    'gustavo henrique rigodanzo canuto' : 55, 
                    'tarcísio gomes de freitas' : 56, 
                    'carlos alberto dos santos cruz' : 57, 
                    'gustavo bebianno' : 58
                    }


def post_news(df):
    use_image = True
          
    for idx in range(len(df)):
        row = df.iloc[idx]
        # date now        
        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date_df = str(row['date'])
        #date_df = datetime.datetime.strptime(row['date'], '%a, %d %b %Y %H:%M:%S %z').strftime("%Y-%m-%d %H:%M:%S")
        
        if(date_df > date_now):
            date = date_df
        else:
            date = date_now
            
        # title for the post
        title = row['titulos']
        # the wordpress categories index for the 'noticia' at idx_noticia index 
        categories_names = row['categorias']
        categories = util.get_categories_idx(categories_names, INDEX_CATEGORIES)
#         cats = util.join_strings(np.array(categories).astype(str).tolist())
        
        # the text of the 'abstract' and the link
        # texto_sumarizado: por enquanto apenas em seguranca
        news = row['abstract']
        reduced_news = util.get_reduced_news(news)
        content = reduced_news + '...'
        
        #testes para o novo formato
#         tupla = relevancia_site_table.select(row['site'])
#         reduced_news = util.get_reduced_news_with_relevance(news, row['site'])
#         temp = '... <p>Leia a íntegra em: ' + '<a href=' + row['links'] +'> ' + row['links']  + '</a>'
        
#         content = reduced_news + temp

#         # if the row does not have category
#         if(categories == []):
#             cats = '1' # category sem categoria
           
#         # url
#         url = URL
# 
#         payload = {'date': date,
#                 'title': title,
#                 'categories': cats,
#                 'content': content,
#                 'status': 'publish',
#                 }
        
        
        
        url = 'http://127.0.0.1:8000/rest/'
        slug = util.slugify_title(title)
        link = row['links']
        payload = {
                "title": title,
                "slug": slug,
                "body": content,
                "abstract": "",
                "date": date,
                "thumb": row["image"],
                "link": link,
                "author": str(1),
                "categories": categories
            }
        
        r = requests.request("POST", url, data=payload)
        print('POST = ' + str(r))
        print(r.text)
                        
#         r = requests.post(url + '/posts', headers=headers, json=post)
#                              
#         if(use_image): 
#             try:
#                 image_path = row['image']
#                 media = {'file': open(image_path,'rb'), 'caption': 'picture'}
#                 image = requests.post(url + '/media', headers=headers, files=media)  
#                 print('IMAGE_POST = ' + str(image))      
#                    
#                 img_id = (json.loads(image.content))['id']
#                 post_id = (json.loads(r.content))['id']
#                 print(img_id)
#                 print(post_id)
#                               
#                 updated_post = {'featured_media' : img_id}
#                                
#                 update = requests.post(url + '/posts/' + str(post_id), headers=headers, json=updated_post)     
#                 print('UPDATE_POST = ' + str(update))
#             except:
#                 print('Image not found.')
