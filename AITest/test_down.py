# -*- coding: utf-8 -*-
from AIFish.d2c import cluster
from AIFish.nlp import nlp
from AIFish.w2v import word2vec
from AIFish.down import fop
import logging
import numpy
import jieba
from gensim import models
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model=models.Word2Vec.load("./ketian/word2vec/word2vec_model")

tableValues=[]
table=[]
words=[x for (x,y) in nlp.word_frequency("./ketian/corpus","./ketian/stopword",word_num=50)]
commons=[x for (x,y) in nlp.word_frequency("./ketian/corpus","./ketian/stopword",word_num=200)]
cluster.word("./ketian/word2vec","./ketian/corpus",words)
dicts_word=cluster.read_cluster_word("./ketian/cluster")

def similar_only(word):
    ret=[]
    similar=model.most_similar(word)
    for value in similar:
        ret.append(value[0])
    return ret[0:5]

def get_string(lists):
    return ",".join(lists)

def get_lines(word):
    lines=[]
    cluster.sentence("./ketian/word2vec","./ketian/corpus",word,commons,10)
    dicts=cluster.read_cluster_sentence("./ketian/cluster",word)
    for value,item in dicts.items():
        for temp in item:
            if len(temp)>=8:
                lines.append(temp)
                break
    return lines

for item,words in dicts_word.items():
    for word in words:
        print("处理：",word)
        for line in get_lines(word):
            dicts={}
            dicts["关键词"]=word
            dicts["同义词"]=get_string(similar_only(word))
            dicts["一级目录"]="科天云知识库"
            dicts["二级目录"]="第"+str(item)+"类"
            dicts["答案"]="请自己填写"
            dicts["问题"]=line
            itrs=jieba.cut(line)
            line_word=[itr for itr in itrs]
            extract=[]
            extract=[key for key in line_word if key in commons]
            keys=numpy.array([model[key] for key in extract])
            keys=numpy.sum(keys,axis=0)/len(extract)
            dicts["语义向量"]=keys
            tableValues.append([dicts['问题'], dicts['答案'], dicts['关键词'], dicts['同义词'],dicts['一级目录'],dicts['二级目录']])
            table.append([dicts['问题'], dicts['答案'], dicts['关键词'], dicts['同义词'],dicts['一级目录'],dicts['二级目录'],dicts['语义向量']])

fop.write_xls(tableValues,"ketian/report",".")
fop.write_pickle("/ketian/report",".",table)