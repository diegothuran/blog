# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import feedparser

GLOBAL_RANK = 86681
RANK_BRAZIL = 2929
NAME = 'jornalopcao.com.br'


def get_urls():
    try:
        urls = [] 
        hit_list = ['https://www.jornalopcao.com.br/feed/']
        
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
        raise Exception('Exception in rss_jornalopcao')



