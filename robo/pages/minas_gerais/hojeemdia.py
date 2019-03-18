# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import feedparser

GLOBAL_RANK = 47746
RANK_BRAZIL = 1683     
NAME = 'hojeemdia.com.br'

def get_urls():
    try:
        urls = [] 
        hit_list = [ 
            'https://www.hojeemdia.com.br/cmlink/geral-completo-1.402774'
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
        raise Exception('Exception in hojeemdia')
