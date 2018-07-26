# -*- coding: utf-8 -*-
import os
import jieba
import logging
from gensim import models
from .exception import TrainError
from .exception import FileError
from .sentences import Sentences

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def train(model_dir,stop_word):
    try:
        sentences=Sentences(model_dir,stop_word)
        model=models.Word2Vec(sentences, workers=20, min_count=50, size=300)
        model.save(model_dir+"/word2vec_model")
    except:
        raise TrainError("词向量训练出错！")
    return True

def vector(model_dir,word):
    try:
        model=models.Word2Vec.load(model_dir+"/word2vec_model")
    except:
        raise FileError("模型文件不存在!")
    return model[word]

def similar_word(model_dir,word):
    try:
        model=models.Word2Vec.load(model_dir+"/word2vec_model")
    except:
        raise FileError("模型文件不存在!")
    return model.most_similar(word)

def similar_only_word(model_dir,word):
    try:
        ret=[]
        model=models.Word2Vec.load(model_dir+"/word2vec_model")
    except:
        raise FileError("模型文件不存在!")
    similar=model.most_similar(word)
    for value in similar:
        ret.append(value[0])
    return ret