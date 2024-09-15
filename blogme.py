# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:50:07 2024

@author: falih
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

# reading excel files (xlsx)

data = pd.read_excel('articles.xlsx')

# summary of the data

data.describe()

# summary of columns

data.info()

# counting articles published per news 

# format by group by 

# df.groupby(['column_to_group'])['column_to_count'].count()


author_count = data.groupby(['source_id'])['article_id'].count()


author_count2 = data.groupby(['source_id']).size()

author_count.describe()

# number of reactions group by publisher

publisher_react = data.groupby(['source_id'])['engagement_reaction_count'].sum()

# # number of shared articles group by publisher

publisher_share = data.groupby(['source_id'])['engagement_share_count'].sum()

# creating bar chart 
publisher_share.plot.bar()
plt.show()

# creating scatterplot chart

ypoint = data['engagement_comment_count']
xpoint = data['engagement_share_count']
plt.scatter(xpoint,ypoint, color = 'red')
plt.show()


# dropping engagement plugin count column

data = data.drop('engagement_comment_plugin_count',axis = 1)




# function in python

def thisfunction():
    print('this is my first function')


thisfunction()


# this is a function with variables (DOODLES)


# def aboutme(name):
#     print('my name is '+name)
#     return name
    
# aboutme('fali')

#  # increment number function (value before, value after)
 
# def increment(x,y):
#     z = (y/x)-1
#     print(z)
#     return round(z * 100,2) 

# a = increment(163,127)


# def tubularvol(d,h):
#     y = 0.5*d
#     z = 3.14 * y * y * h
#     print(z)
#     return round(z,2)

# tubularvol(5,15)


# tubularvol(3,12)


# def vol_kerucut(d,h):
#     r = 0.5*d
#     vol=(1/3)*(3.143782378*r*r)*(h)
#     print(vol)

# vol_kerucut(5,12)


# increment(150,178)


# # function with str

# def tentangsaya(x,y,z):
#     print('my name is '+ x +' tinggal di '+ y + ' jenis kelamin '+ z)
#     return x,y,z
    
# tentangsaya('falih','jakarta','pria')


# saldo = []




# def masukan(x,y):
#     z = x-y 
#     print (z)
#     saldo.append(z)
#     return z
#     print(saldo)

# masukan(150,134)
# masukan(150,99)
# masukan(150,127)
# masukan(150,101)

# print(saldo)



# using for loops in functions
warteg_food=['orek','balado','ikan asap']
def favfood(food):
    for x in warteg_food:
        print('the top food is '+x)
    

favfood(warteg_food)


# creating a keyword flag

keyword = 'crash'

# for loop functions for isolate each title row
length = len(data)

# keyword = 'crash'
# keyword_flag = []
# for x in range(0,length):
#     heading = data['title'][x]
#     if keyword in heading: 
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)

length = len(data)   
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading: 
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
keywordflag =  keywordflag('murder')

# creating a new column in data dataframe

data['keyword_flag'] = keywordflag

# SentimentIntensityAnalyzer 

sent_int = SentimentIntensityAnalyzer ()

text = data['title'][15]

sent = sent_int.polarity_scores(text)

text = data['title'][16]

sent = sent_int.polarity_scores(text)


neg = sent['neg'] #menarik baris dari dictionary file
pos = sent['pos']
neu = sent['neu']


# using for loops to extract positive, negative and neutral sentiment from headline text
length = len(data)
neg_sentiment_title = []
pos_sentiment_title = []
neu_sentiment_title = []

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    neg_sentiment_title.append(neg)
    pos_sentiment_title.append(pos)
    neu_sentiment_title.append(neu)
    
data['neg_sentiment_title'] = neg_sentiment_title

title_neg_sentiment = pd.Series(neg_sentiment_title) #mengubah variable menjadi series


# inserting variables into data columns

data['neg_sentiment_title'] = neg_sentiment_title
data['pos_sentiment_title'] = pos_sentiment_title
data['neu_sentiment_title'] = neu_sentiment_title


# exporting to xlsx

data.to_excel('blogme_clean.xlsx',sheet_name = 'blogmedata', index = False)