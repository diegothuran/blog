#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import base64
import datetime
import numpy as np


url = 'http://127.0.0.1:8000/rest/'
 
payload = {
        "title": "postagem via api2",
        "slug": "postagem-via-api2",
        "body": "Primeiro post via API2.",
        "abstract": "",
        "date": "2019-03-12T00:57:00Z",
        "thumb": "",
        "link": "",
        "author": str(1),
        "categories": [1]
    }

response = requests.request("POST", url, data=payload)
print(response.text)
