# -*- coding: utf-8 -*-
import jieba
import pickle
import logging
import numpy
from AIFish.down import fop
from gensim import models
from AIFish.nlp import nlp
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model=models.Word2Vec.load("./ketian/word2vec/word2vec_model")

i=0
temp=[]
sentences=[]
tableValues=fop.read_pickle("/ketian/report",".")
for dicts in tableValues:
    sentences.append([0,dicts[6],i])
    i=i+1
commons=[x for (x,y) in nlp.word_frequency("./ketian/corpus","./ketian/stopword",word_num=200)]
input_str=input("请输入：")
itrs=jieba.cut(input_str)l
line_word=[itr for itr in itrs]
extract=[]
extract=[key for key in line_word if key in commons]
keys=numpy.array([model[key] for key in extract])
keys=numpy.sum(keys,axis=0)/len(extract)
for item in sentences:
    item[0]=numpy.sqrt(numpy.sum(numpy.square(keys - item[1])))
for item in sentences:
    temp.append((item[0],item[2]))
temp.sort()
temp=temp[0:5]
for item in temp:
    print("------------------------")
    print(tableValues[item[1]][0])