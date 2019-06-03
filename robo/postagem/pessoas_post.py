#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import json
# import base64
import datetime
import numpy as np

from robo.Util import util

URL = 'http://127.0.0.1:8000/rest/'

def post_news(info):
    date_now = datetime.datetime.now()
    if(info['date'][0] > date_now):
        date = info['date'][0]
    else:
        date = date_now
    
    str_date = date.strftime("%Y-%m-%d %H:%M:%S")
    
    news = info['body'][0]
    reduced_news = util.get_reduced_news(news)
    content = reduced_news + '...'
    
    if(info['thumb'] == '0'):
        img = ''
    else:
        img = info['thumb']
    
    payload = {
            "title": info['title'][0],
            "slug": info['slug'][0],
            "body": content,
            "abstract": "",
            "date": str_date,
            "thumb": img,
            "link": info['link'][0],
            "author": str(1),
            "categories": info['categories']
        }
    
    r = requests.request("POST", URL, data=payload)
    print('POST = ' + str(r))
    print(r.text)
        