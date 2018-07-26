# -*- coding: utf-8 -*-
import os
import jieba
from .exception import TrainError

class Sentences(object):

    def __init__(self, model_dir,stop_word):
        self.model_dir = model_dir
        self.stop_word=stop_word

    def __iter__(self):
        for filename in os.listdir(self.model_dir):
            file_path = self.model_dir + "/" + filename
            if "word2vec_model" not in file_path:
                for line in open(file_path,"rb"):
                    try:
                        line=str(line,"utf-8")
                    except:
                        raise TrainError("词向量训练出错!")
                    words = jieba.cut(line)
                    result_word = []
                    for word in words:
                        if word not in self.stop_word:
                            result_word.append(word)
                    yield result_word