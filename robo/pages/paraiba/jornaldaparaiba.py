# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import feedparser

GLOBAL_RANK = 110038
RANK_BRAZIL = 3508    
NAME = 'jornaldaparaiba.com.br'


def get_urls():
    try:
        urls = [] 
        hit_list = [ 
            'http://www.jornaldaparaiba.com.br/feed'
            ]
    
        future_calls = [feedparser.parse(rss_url) for rss_url in hit_list]

        entries = []
        for feed in future_calls:
            entries.extend(feed["items"])

        for entrie in entries:
            ref_link = entrie['link']
            urls.append(ref_link)
        
        return urls
    except:
        raise Exception('Exception in jornaldaparaiba')
