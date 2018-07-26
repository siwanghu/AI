# -*- coding: utf-8 -*-
import os
import jieba
import nltk
import scipy
import pickle
from jieba import posseg
from wordcloud import WordCloud
from .exception import FileError

def cut_word(input_str):
    words=[]
    for word in jieba.cut(input_str):
        words.append(word)
    return words

def word_posseg(input_str,possegs=['v','n','a']):
    words=[]
    for word,poss in posseg.cut(input_str):
        if poss in possegs:
            words.append(word)
    return words

def idf(corpus_dir,word):
    try:
        corpus_idf=pickle.load(open(corpus_dir+"/IDF.txt","rb"))
        return corpus_idf[word]
    except:
        raise FileError("IDF序列化文件不存在")

def tf(input_str):
    tf_dict={}
    words=[word for word in jieba.cut(input_str)]
    for word in words:
        if word not in tf_dict.keys():
            tf_dict[word]=words.count(word)
    return tf_dict

def __read_filter_dir(filter_dir):
    stop_words=[]
    for filename in os.listdir(filter_dir):
        file_path = filter_dir + "/" + filename
        with open(file_path,"rb") as file_read:
            line=str(file_read.readline(),"utf-8").replace("\r\n","").replace("\n","")
            while line:
                stop_words.append(line)
                line=str(file_read.readline(),"utf-8").replace("\r\n","").replace("\n","")
    return stop_words

def __read_corpus_dir(corpus_dir,stop_words):
    result_words=[]
    for filename in os.listdir(corpus_dir):
        file_path = corpus_dir + "/" + filename
        if "IDF.txt" not in file_path:
            with open(file_path,"rb") as file_read:
                line=str(file_read.readline(),"utf-8").replace("\r\n","").replace("\n","")
                while line:
                    for word in jieba.cut(line):
                        if word not in stop_words:
                            result_words.append(word)
                    line=str(file_read.readline(),"utf-8").replace("\r\n","").replace("\n","")
    return result_words

def __WordCloud(imgPath,corpus_dir,words):
    img=scipy.misc.imread(imgPath)
    cloud=WordCloud(font_path="simkai.ttf",
                    background_color='white',
                    mask=img,
                    max_words=50,
                    max_font_size=200)
    cloud.generate(" ".join(words))
    report_dir=corpus_dir.replace("corpus","report")
    cloud.to_file(report_dir+"/ciyun.jpg")
    return True

def draw_WordCloud(imgPath,corpus_dir,filter_dir):
    stop_words=__read_filter_dir(filter_dir)
    result_words=__read_corpus_dir(corpus_dir,stop_words=stop_words)
    __WordCloud(imgPath,corpus_dir,words=result_words)
    return True

def word_frequency(corpus_dir,filter_dir,word_num=100):
    stop_words=__read_filter_dir(filter_dir)
    result_words=__read_corpus_dir(corpus_dir,stop_words=stop_words)
    return nltk.probability.FreqDist(result_words).most_common(word_num)

def extract_keyword(input_str,corpus_dir,key_num=10):
    result=[]
    corpus_idf=pickle.load(open(corpus_dir+"/IDF.txt","rb"))
    str_tf=tf(input_str)
    for word in str_tf.keys():
        str_tf[word]=str_tf[word]*corpus_idf[word]
    for word,tfidf in str_tf.items():
        result.append((tfidf,word))
    result.sort(reverse=True)
    return [word for tfidf,word in result][:key_num]