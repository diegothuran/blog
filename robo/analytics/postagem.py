#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import base64
import datetime
import numpy as np


url = 'http://127.0.0.1:8000/rest/'
 
payload = {
        "title": "postagem via api",
        "slug": "postagem-via-api",
        "body": "Primeiro post via API.",
        "abstract": "",
        "date": "2019-05-29T20:57:00Z",
        "thumb": "",
        "link": "https://www.uol.com.br/",
        "author": str(1),
        "categories": [2,3,4]
    }

response = requests.request("POST", url, data=payload)
print(response.text)
