# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import feedparser

GLOBAL_RANK = 10662
RANK_BRAZIL = 230
NAME = 'senado.leg.br'

def get_urls():
    try:
        urls = [] 
        hit_list = ['https://www12.senado.leg.br/noticias/feed/todasnoticias/RSS']
        
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
        raise Exception('Exception in rss_senado')

