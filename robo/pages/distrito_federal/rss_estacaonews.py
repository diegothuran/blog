# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import feedparser

GLOBAL_RANK = None
RANK_BRAZIL = None
NAME = 'estacaonews.blog.br'

def get_urls():
    try:
        urls = [] 
        hit_list = ['http://estacaonews.blog.br/feed/']
        
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
        raise Exception('Exception in estacaonews')
