# -*- coding: utf-8 -*-
import os
import numpy
import jieba
import pickle
from gensim import models
from sklearn.cluster import KMeans
from .exception import FileError

def read_cluster_word(cluster_dir):
    try:
        dicts=pickle.load(open(cluster_dir+"/"+"词向量聚类.txt","rb"))
        return dicts
    except:
        raise FileError("词向量聚类文件不存在")

def read_cluster_sentence(cluster_dir,word):
    try:
        dicts=pickle.load(open(cluster_dir+"/"+word+"_语义向量聚类.txt","rb"))
        return dicts
    except:
        raise FileError("语义向量聚类文件不存在")

def word(model_dir,corpus_dir,words,n_clusters=25):
    dicts={}
    result=[]
    cluster_dir=corpus_dir.replace("corpus","cluster")
    model = models.Word2Vec.load(model_dir+"/word2vec_model")
    features=[model[word] for word in words]
    k_means = KMeans(n_clusters=n_clusters)
    k_model=k_means.fit(features)
    for _ in range(n_clusters):
        dicts[_]=[]
    for _ in range(len(k_model.labels_)):
        result.append((k_model.labels_[_],words[_]))
    for token in result:
        dicts[token[0]].append(token[1])
    pickle.dump(dicts,open(cluster_dir+"/"+"词向量聚类.txt","wb"))
    return True

def split_question(corpus_dir,words):
    file_dicts={}
    cluster_dir=corpus_dir.replace("corpus","cluster")
    for word in words:
        file_dicts[word]=open(cluster_dir+"/"+word+".txt","w",encoding="utf-8")
    for filename in os.listdir(corpus_dir):
        file_path = corpus_dir + "/" + filename
        if "IDF" not in file_path:
            with open(file_path,"rb") as file_read:
                line=str(file_read.readline(),"utf-8")
                while line:
                    itrs=jieba.cut(line)
                    line_word=[itr for itr in itrs if itr in words]
                    for word in words:
                        if word in line_word:
                            file_dicts[word].writelines(line)
                            break
                    line=file_read.readline()
                    line=str(line,"utf-8")
    for word in file_dicts.keys():
        file_dicts[word].close() 
    return True

def sentence(model_dir,corpus_dir,word,words,n_clusters):
    lines=[]
    result=[]
    cluster_dir=corpus_dir.replace("corpus","cluster")
    model = models.Word2Vec.load(model_dir+"/word2vec_model")
    with open(cluster_dir+"/"+word+".txt","rb") as file:
        line=str(file.readline(),"utf-8").replace("\r\n","").replace("\n","").replace("\r","")
        while line:
            itrs=jieba.cut(line)
            line_word=[itr for itr in itrs]
            extract=[]
            try:
                extract=[key for key in line_word if key in words]
                keys=numpy.array([model[key] for key in extract])
            except:
                line=file.readline()
                line=str(line,"utf-8").replace("\r\n","").replace("\n","").replace("\r","")
                continue
            keys=numpy.sum(keys,axis=0)/len(extract)
            lines.append((line,keys,extract))
            line=file.readline()
            line=str(line,"utf-8").replace("\r\n","").replace("\n","").replace("\r","")
    features=[y for (x,y,z) in lines]
    k_means = KMeans(n_clusters=n_clusters)
    k_model=k_means.fit(features)
    ids=k_model.cluster_centers_
    for index in range(len(k_model.labels_)):
        result.append((k_model.labels_[index],lines[index][0]))
    dicts,clusters={},n_clusters
    for _ in range(clusters):
        dicts[_]=[]
    for result in result:
        dicts[result[0]].append(result[1])
    pickle.dump(dicts,open(cluster_dir+"/"+word+"_语义向量聚类.txt","wb"))
    return True