# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import feedparser

GLOBAL_RANK = 558617
RANK_BRAZIL = 22699
NAME = 'diariobahia.com.br'

def get_urls():
    try:
        urls = [] 
        hit_list = ['http://diariobahia.com.br/feed/']
        
        future_calls = [feedparser.parse(rss_url) for rss_url in hit_list]
        
        entries = []
        for feed in future_calls:
            entries.extend(feed["items"])
        
        for entrie in entries:
            ref_link = entrie['link']
#             print(ref_link)
            urls.append(ref_link)
        
        return urls
    except:
        raise Exception('Exception in diariobahia')

