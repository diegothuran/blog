#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest


from Database import connection, relevancia_site_table
import nltk
import re

import numpy as np
import math

# def sent_tokenize_texto_foto(article_text):
#     sentence_list = nltk.sent_tokenize(article_text)
#     
#     if('foto' in sentence_list[0].lower()):  
#         sentence_list.pop(0)
#     return sentence_list

def sent_tokenize_texto_foto(article_text):
    sentence_list = nltk.sent_tokenize(article_text)
    idx = None
    for i in range(len(sentence_list[:3])):
        if('foto' in sentence_list[i].lower()):  
            idx = i
    if(idx is not None):
        sentences = sentence_list[idx+1:]
    else:
        sentences = sentence_list
    return sentences

def sumarizar(article_text):
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
    article_text = re.sub(r'\s+', ' ', article_text)  
    
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)  
    
#     sentence_list = nltk.sent_tokenize(article_text)
#     
#     if('foto' in sentence_list[0].lower()):  
#         sentence_list.pop(0)
    sentence_list = sent_tokenize_texto_foto(article_text)
#     stopwords = nltk.corpus.stopwords.words('english')
    stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))
#     stopwords = set(nltk.corpus.stopwords.words('portuguese'))

    word_frequencies = {}  
    for word in nltk.word_tokenize(formatted_article_text):  
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    
    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    sentence_scores = {}  
    for sent in sentence_list:  
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 45:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
                        
    summary_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)  
    print(summary)  
    
    
def sumarizar_nltk(texto):
#     sentencas = sent_tokenize(texto)
    sentencas = sent_tokenize_texto_foto(texto)
    palavras = word_tokenize(texto.lower())
        
#     stopwords = set(stopwords.words('portuguese') + list(punctuation))
    stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]
    
    frequencia = FreqDist(palavras_sem_stopwords)
    
    sentencas_importantes = defaultdict(int)
    
    for i, sentenca in enumerate(sentencas):
        for palavra in word_tokenize(sentenca.lower()):
            if palavra in frequencia:
                sentencas_importantes[i] += frequencia[palavra]

    idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)

    for i in sorted(idx_sentencas_importantes):
        print(sentencas[i])

def sumarizar_towards(article_text):
    'https://towardsdatascience.com/how-to-learn-more-in-less-time-with-natural-language-processing-part-1-49d94543f73d'
    #Remove special characters, numbers, stopwords, etc. from the text
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
    article_text = re.sub(r'\s+', ' ', article_text)  
        
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)  
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    
    words = word_tokenize(formatted_article_text) 
#     stopWords = nltk.corpus.stopwords.words('english')
#     stopWords = set(nltk.corpus.stopwords.words('portuguese'))
    stopWords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))
    
    #Tally word frequencies from the text
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    
    #Break text into sentences then assign values based on word frequencies
#     sentences = sent_tokenize(article_text)
    sentences = sent_tokenize_texto_foto(article_text)
    sentenceValue = dict()
        
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
        
        
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    
    # Average value of a sentence from original text
    average = int(sumValues / len(sentenceValue))
        
    #If a sentence's value exceeds the average * 1.2, include it in the summary
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
                
    #Print summary and analytics
#     print("Original article URL: " + url + "\n")
    print(summary + "\n")
#     print("Original word count: " + str(len(article_text.split())))
#     print("Summarized word count: " + str(len(summary.split())))
#     print("Percent reduction: " + str("%.2f" % (100 - len(summary.split()) * 100 / len(article_text.split()))) + "%")
#     print("Time reduction: " + str("%.0f" % (len(article_text.split()) / 225)) + " minutes to " + str("%.0f" % (len(summary.split()) / 225)) + " minutes")

# def remove_string_special_characters(s):
#     stripped = re.sub('[^\w\s', '', s)
#     stripped = re.sub('_', '', stripped)
#     
#     stripped = re.sub('\s+', ' ', stripped)
#     
#     stripped = stripped.strip()
#     return stripped

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
    
def get_textos():
    categoria = 'osmar terra'
    textos = relevancia_site_table.select_text_categories(categoria)
    print(len(textos))
    from gensim.summarization.summarizer import summarize
    for texto in textos:
        print('\n --- TEXTO ORIGINAL --- ')
        print(texto[0])
        print('\n --- SUMARIO NLTK --- ')
        sumarizar_nltk(texto[0])
        print('\n --- SUMARIO --- ')
        sumarizar(texto[0])
        print('\n --- SUMARIO - TOWARDS --- ')
        sumarizar_towards(texto[0])
        
        print('\n --- SUMARIO - TFIDF --- ')
        text_sents = sent_tokenize(texto[0])
        text_sents = sent_tokenize_texto_foto(texto[0])
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
        

if __name__ == '__main__':
    get_textos()