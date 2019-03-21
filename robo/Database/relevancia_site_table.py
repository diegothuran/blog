#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../src')
from robo.Model import Relevancia_Site
from robo.Database import connection
import datetime
from dateutil import parser
# import robo.postagem.Util as Util

from pandas import DataFrame


def save(relevancia_site = Relevancia_Site):
    cnx = connection.connection()

    try:
        cursor = cnx.cursor()
        
        add_news = ("INSERT INTO relevancia_site "
                    "(id, site, relevancia, relevancia_inicial) "
                        "VALUES (NULL, %s, %s, %s)", (relevancia_site.site[0], relevancia_site.relevancia[0], relevancia_site.relevancia_inicial[0]))

        cursor.execute(*add_news)
    except Exception as e:
        print(e)

    cnx.close()

def select(site):
    cnx = connection.connection()
    cursor = cnx.cursor()
  
    sql = "SELECT * FROM relevancia_site WHERE site = %s"
    site = (site, )    
    cursor.execute(sql, site)
    result = cursor.fetchall()[0] 
    cnx.close()
    return result

def check(relevancia_site = Relevancia_Site):
    cnx = connection.connection()
     
    cursor = cnx.cursor()
 
    sql = "SELECT * FROM relevancia_site WHERE site = %s"
    site = (relevancia_site.site[0], )    
    cursor.execute(sql, site)
  
    rows = cursor.fetchall()
    if(len(rows) > 0):
        site_in_db = True
    else:
        site_in_db = False
     
    cnx.close()
    return site_in_db

def update(relevancia_site = Relevancia_Site):
    cnx = connection.connection()
     
    cursor = cnx.cursor()
    
    sql = "UPDATE relevancia_site SET relevancia = %s WHERE site = %s"
    site = (relevancia_site.relevancia[0], relevancia_site.site[0],)    
    cursor.execute(sql, site)
    
    cnx.close()
    
def update_com_relevancia_inicial(relevancia_site = Relevancia_Site):
    cnx = connection.connection()
     
    cursor = cnx.cursor()
    
    sql = "UPDATE relevancia_site SET relevancia = %s, relevancia_inicial = %s WHERE site = %s"
    site = (relevancia_site.relevancia[0], relevancia_site.relevancia_inicial[0], relevancia_site.site[0],)    
    cursor.execute(sql, site)
    
    cnx.close()

def select_form_date(request_date):
    cnx = connection.connection()
     
    cursor = cnx.cursor()
    
    query = ("SELECT * FROM pessoas "
             "WHERE public_date = %s")
    
    str_date = request_date.strftime("%Y-%m-%d")
#     hire_start = datetime.date(1999, 1, 1)
#     hire_end = datetime.date(1999, 12, 31)
    str_date = (str_date, )    
    cursor.execute(query, str_date)
    rows = cursor.fetchall()
    print(len(rows))
    
    cursor.close()
    cnx.close()
    return len(rows)
    
def select_site_in_link(site):
    cnx = connection.connection()
     
    cursor = cnx.cursor()
    
#     query = ("SELECT * FROM pessoas WHERE id = %s AND link LIKE %s")
#     formated_string = '%' + site + '%'
#     request_site = ('1', formated_string, )    
    
    query = ("SELECT * FROM pessoas WHERE link LIKE %s")
    formated_string = '%' + site + '%'
    request_site = (formated_string, )    
    
    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
#     print(len(rows))
    for row in rows:
        print(row)
    
    cursor.close()
    cnx.close()
    
def update_site(site):
    cnx = connection.connection()
    cursor = cnx.cursor()

    query = ("UPDATE pessoas SET site = %s WHERE link LIKE %s")
     
    formated_string = '%' + site + '%'
    val = (site, formated_string, )    
    cursor.execute(query, val)
    
    cnx.commit()

    print(cursor.rowcount, "record(s) affected") 
     
    cursor.close()
    cnx.close()
    
def select_site(site):
    cnx = connection.connection()
    cursor = cnx.cursor()
    
    query = ("SELECT * FROM pessoas WHERE site = %s")
    request_site = (site, )    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
#     print(len(rows))
    for row in rows:
        print(row)
    
    cursor.close()
    cnx.close()
    
def select_categories(categories):
    cnx = connection.connection()     
    cursor = cnx.cursor()
        
    if(len(categories) == 1):
        query = ("SELECT categories FROM pessoas WHERE categories LIKE %s")
        formated_string = '%' + categories[0] + '%'
        request_site = (formated_string, )    
    else:
        formated_strings = ()
        for i in range(len(categories)):
            formated_string = ('%' + categories[i] + '%', )
            formated_strings = formated_strings + formated_string
            if(i == 0):
                query_condition = 'categories LIKE %s '
            else:
                query_condition += ' AND categories LIKE %s ' 
        query = ("SELECT categories FROM pessoas WHERE " + query_condition)
        request_site = formated_strings
        
#     query = ("SELECT categories FROM pessoas WHERE categories LIKE %s AND categories LIKE %s")
#     formated_string = '%' + categories[0] + '%'
#     formated_string2 = '%' + categories[1] + '%'
#     request_site = (formated_string, formated_string2)
    
#     print(query)
#     print(request_site)
    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
#     print(len(rows))
    for row in rows:
        print(row)
    
    cursor.close()
    cnx.close()
    return rows

def select_text_categories(category):
    cnx = connection.connection()     
    cursor = cnx.cursor()

    query = ("SELECT abstract FROM pessoas WHERE categories LIKE %s")
    formated_string = '%' + category + '%'
    request_site = (formated_string, )    
    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
#     print(len(rows))
    for row in rows:
        print(row)
    
    cursor.close()
    cnx.close()
    
    return rows

def select_news_source_categories(categories):
    cnx = connection.connection()     
    cursor = cnx.cursor()

    if(len(categories) == 1):
        query = ("SELECT site FROM pessoas WHERE categories LIKE %s")
        formated_string = '%' + categories[0] + '%'
        request_site = (formated_string, )    
    else:
        formated_strings = ()
        for i in range(len(categories)):
            formated_string = ('%' + categories[i] + '%', )
            formated_strings = formated_strings + formated_string
            if(i == 0):
                query_condition = 'categories LIKE %s '
            else:
                query_condition += ' AND categories LIKE %s ' 
        query = ("SELECT site FROM pessoas WHERE " + query_condition)
        request_site = formated_strings
    
#     query = ("SELECT site FROM pessoas WHERE categories LIKE %s")
#     formated_string = '%' + category + '%'
#     request_site = (formated_string, )    
    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    cnx.close()
    
    return rows    

def get_categories_per_site(site):
    cnx = connection.connection()
    cursor = cnx.cursor()
    
    query = ("SELECT categories FROM pessoas WHERE site = %s")
    request_site = (site, )    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
#     print(len(rows))
    for row in rows:
        print(row)
    
    cursor.close()
    cnx.close()
    
    return rows
    
# def select_site_pd(site):
#     cnx = connection.connection()
#     cursor = cnx.cursor()
#     
#     query = ("SELECT * FROM pessoas WHERE site = %s")
#     request_site = (site, )    
#     cursor.execute(query, request_site)
#     rows = cursor.fetchall()
#     print(len(rows))
#     for row in rows:
#         print(row)
#     df = DataFrame(rows)
# #     print(df)
# #     df.columns = rows.keys()
#     
# #     print(df.iloc[:,8])
#     cursor.close()
#     cnx.close()
#     
#     categories = df.iloc[:,8]
#     return categories


def get_interval(data_inicial, data_final):
    cnx = connection.connection()
    cursor = cnx.cursor()
    
    query = ("SELECT public_date FROM pessoas "
             "WHERE public_date BETWEEN %s AND %s")
    
#     str_data_inicial = data_inicial.strftime("%Y-%m-%d")
#     str_data_final = data_final.strftime("%Y-%m-%d")
    request_site = (data_inicial, data_final, )    
    cursor.execute(query, request_site)
    
    rows = cursor.fetchall()
#     print(len(rows))
#     print('aqui')
    for i in rows:
        print(i)
    
#     for (first_name, last_name, hire_date) in cursor:
#         print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))
    
    cursor.close()
    cnx.close()
    
    return rows
    
def get_interval_category(categories, data_inicial, data_final):
    cnx = connection.connection()
    cursor = cnx.cursor()
    
    if(len(categories) == 1):
        query = ("SELECT public_date FROM pessoas WHERE categories LIKE %s AND public_date BETWEEN %s AND %s")
        formated_string = '%' + categories[0] + '%'
        request_site = (formated_string, data_inicial, data_final, )      
    else:
        formated_strings = ()
        for i in range(len(categories)):
            formated_string = ('%' + categories[i] + '%', )
            formated_strings = formated_strings + formated_string
            if(i == 0):
                query_condition = 'categories LIKE %s '
            else:
                query_condition += ' AND categories LIKE %s ' 
        query = ("SELECT public_date FROM pessoas WHERE " + query_condition + "AND public_date BETWEEN %s AND %s")
        request_site = formated_strings + (data_inicial,) + (data_final,)
        
    print(query)
    print(request_site)
    
#     query = ("SELECT public_date FROM pessoas "
#              "WHERE categories LIKE %s AND public_date BETWEEN %s AND %s")
#     
# #     query = ("SELECT * FROM pessoas "
# #              "WHERE categories LIKE %s AND public_date BETWEEN %s AND %s")
#     
# #     str_data_inicial = data_inicial.strftime("%Y-%m-%d")
# #     str_data_final = data_final.strftime("%Y-%m-%d")
#     request_site = (category, data_inicial, data_final, )    

    cursor.execute(query, request_site)
    rows = cursor.fetchall()

    for i in rows:
        print(i)
    
#     for (first_name, last_name, hire_date) in cursor:
#         print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))
    
    cursor.close()
    cnx.close()    
    
    return rows
    