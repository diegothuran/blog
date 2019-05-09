#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../../blog')
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
