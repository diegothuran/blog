#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import math
from coverage import summary

text1 = """
    If you like tuna and tomato sauce-try combining the two.
    It's really not as bad as it sounds.
    If the Easter Bunny and the Tooth Fairy had babies would they take
    you teeth and leave chocolate for you?
    """ 

def remove_string_special_characters(s):
#     stripped = re.sub('[^\w\s', '', s)
#     stripped = re.sub('_', '', stripped)
#     
#     stripped = re.sub('\s+', ' ', stripped)
#     
#     stripped = stripped.strip()
#     return stripped

    article_text = re.sub(r'\[[0-9]*\]', ' ', s)  
    article_text = re.sub(r'\s+', ' ', article_text)  
        
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)  
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    stripped = formatted_article_text.strip()
    return stripped

def get_doc(text_sents_clean):
    doc_info = []
    i = 0
    
    for sent in text_sents_clean:
        i+=1
        count = count_words(sent)
        temp = {'doc_id':i, 'doc_length':count}
        doc_info.append(temp)
    return doc_info

def count_words(sent):
    count = 0
    words = word_tokenize(sent)
    for word in words:
        count +=1
    return count

def create_freq_dict(sents):
    i = 0
    freqDict_list = []
    for sent in sents:
        i+= 1
        freq_dict = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            if(word in freq_dict):
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
            temp = {'doc_id':i, 'freq_dict' : freq_dict}
        freqDict_list.append(temp)
    return freqDict_list

def computeTF(doc_info, freqDict_list):
    TF_scores = []
    for tempDict in freqDict_list:
        id = tempDict['doc_id']
        for k in tempDict['freq_dict']:
            temp = {'doc_id' : id,
                    'TF_score' : tempDict['freq_dict'][k]/doc_info[id-1]['doc_length'],
                    'key' : k}
            TF_scores.append(temp)
    return TF_scores

def computeIDF(doc_info, freqDict_list):
    IDF_scores = []
    counter = 0
    for dict in freqDict_list:
        counter += 1
        for k in dict['freq_dict'].keys():
            count = sum([k in tempDict['freq_dict'] for tempDict in freqDict_list])
            temp = {'doc_id':counter, 'IDF_score':math.log(len(doc_info)/count), 'key':k}

            IDF_scores.append(temp)
    return IDF_scores

def computeTFIDF(TF_scores, IDF_scores):
    TFIDF_scores = []
    for j in IDF_scores:
        for i in TF_scores:
            if j['key'] == i['key'] and j['doc_id'] == i['doc_id']:
                temp = {'doc_id':j['doc_id'], 'TFIDF_score': j['IDF_score']*i['TF_score'], 'key': i['key']}
        TFIDF_scores.append(temp)
    return TFIDF_scores

def get_sent_score(TFIDF_scores, text_sents, doc_info):
    sentence_info = []
    for doc in doc_info:
        """
        This loops through each document (sentence) and calculates their sent_score
        """
        sent_score = 0
        for i in range(len(TFIDF_scores)):
            temp_dict = TFIDF_scores[i]
            if(doc['doc_id'] == temp_dict['doc_id']):
                sent_score += temp_dict['TFIDF_score']
        temp = {'doc_id': doc['doc_id'], 'sent_score' : sent_score,
                'sentence' : text_sents[doc['doc_id'] - 1]}
        sentence_info.append(temp)
    return sentence_info

def get_summary(sentence_info):
    sum = 0
    summary, array = [], []
    for temp_dict in sentence_info:
        sum += temp_dict['sent_score']
    avg = sum/len(sentence_info) #computing the average tf-idf score
    for temp_dict in sentence_info:
        array.append(temp_dict['sent_score'])
    std = np.std(array)
    for sent in sentence_info:
#         if(sent['sent_score']) >= avg: # +3*std
        if(sent['sent_score']) >= avg: # +1.5*std
            summary.append(sent['sentence'])
    summary = '\n'.join(summary)
    return summary


text_sents = sent_tokenize(text1)
text_sents_clean = [remove_string_special_characters(s) for s in text_sents]
# document, aka sentence.
doc_info = get_doc(text_sents_clean)

freqDict_list = create_freq_dict(text_sents_clean)
TF_scores = computeTF(doc_info, freqDict_list)
IDF_scores = computeIDF(doc_info, freqDict_list)
TFIDF_scores = computeTFIDF(TF_scores, IDF_scores)

sentence_info = get_sent_score(TFIDF_scores, text_sents, doc_info)

summary = get_summary(sentence_info)
print(summary)

