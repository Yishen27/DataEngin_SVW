# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:30:10 2021

@author: mrluy
"""

import pandas as pd
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize

data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
#print(data)

transaction = []
item_count = {}

for i in range(data.shape[0]):
    temp = []
    for j in range(data.shape[1]):
        item = str(data.values[i, j])
        if item != 'nan':
            temp.append(item)
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
    transaction.append(temp)
    
#print(transaction)
#print(item_count)
    
def remove_stop_word(f):
    stop_words = []
    for sw in stop_words:
        f = f.replace(sw, '')
    
    return f

def Word_cloud(f):
    f = remove_stop_word(f)
    cut_text = word_tokenize(f)
    cut_text = " ".join(cut_text)
    
    wc = WordCloud(max_words = 100, width = 2000, height = 1200)
    wordcloud = wc.generate(cut_text)
    wordcloud.to_file("wc.jpg")
    
all_word = ' '.join('%s' %item for item in transaction)
Word_cloud(all_word)
    
    
    
    
    
    
    
    
    