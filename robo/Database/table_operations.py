#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../../blog')

from robo.Model import News
from robo.Database import connection
from dateutil import parser


def check_news(news = News):
    cnx = connection.connection()
    cursor = cnx.cursor()

    sql = "SELECT * FROM articles_article WHERE title = %s"
    titulo = (news.title[0], )    
#     a = 'postagem via api'
#     titulo = (a, )
    print(titulo)
    cursor.execute(sql, titulo)
 
    rows = cursor.fetchall()
    if(len(rows) > 0):
        news_in_db = True
    else:
        news_in_db = False
    
    cnx.close()
    return news_in_db

def select_form_date(request_date):
    cnx = connection.connection()
    cursor = cnx.cursor()
    
    query = ("SELECT * FROM pessoas "
             "WHERE public_date = %s")
    
    str_date = request_date.strftime("%Y-%m-%d")

    str_date = (str_date, )    
    cursor.execute(query, str_date)
    rows = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    return len(rows)
    

def select_site_in_link(link):
    cnx = connection.connection()
    cursor = cnx.cursor()    
    
    query = ("SELECT site FROM pessoas WHERE link LIKE %s")
    formated_string = '%' + link + '%'
    request_site = (formated_string, )    
    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    return rows


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
    
# def select_site(site):
#     cnx = connection.connection()
#     cursor = cnx.cursor()
#     
#     query = ("SELECT * FROM pessoas WHERE site = %s")
#     request_site = (site, )    
#     cursor.execute(query, request_site)
#     rows = cursor.fetchall()
#     
#     cursor.close()
#     cnx.close()
    
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
    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
    
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
    
    cursor.execute(query, request_site)
    rows = cursor.fetchall()
    
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
    for row in rows:
        print(row)
    
    cursor.close()
    cnx.close()
    
    return rows
    
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
    for i in rows:
        print(i)
    
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

    cursor.execute(query, request_site)
    rows = cursor.fetchall()

    cursor.close()
    cnx.close()    
    
    return rows
    