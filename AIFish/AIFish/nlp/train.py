# -*- coding: utf-8 -*-
import os
import math
import jieba
import pickle

def idf(corpus_dir,corpus_num):
    file_words=[]
    corpus_idf={}
    for filename in os.listdir(corpus_dir):
        file_path = corpus_dir + "/" + filename
        if "IDF.txt" not in file_path:
            with open(file_path,"rb") as file_read:
                line=str(file_read.readline(),"utf-8-sig").replace("\r\n","").replace("\n","")
                while line:
                    file_words.append([word for word in jieba.cut(line)])
                    line=str(file_read.readline(),"utf-8-sig").replace("\r\n","").replace("\n","")
    for words in file_words:
        for word in words:
            if word not in corpus_idf.keys():
                line_num=0
                for line in file_words:
                    if word in line:
                        line_num=line_num+1
                corpus_idf[word]=math.log(corpus_num/(line_num+1))
    pickle.dump(corpus_idf,open(corpus_dir+"/IDF.txt","wb"))
    return True