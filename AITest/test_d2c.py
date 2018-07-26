# -*- coding: utf-8 -*-
from AIFish.d2c import cluster
from AIFish.nlp import nlp
from AIFish.w2v import word2vec

def test_d2c():
    words=[x for (x,y) in nlp.word_frequency("./corpus","./stopword")]
    print(cluster.word("./word2vec","./corpus",words))
    print(cluster.read_cluster_word("./cluster"))
    print(cluster.split_question("./corpus",words))
    print(cluster.sentence("./word2vec","./corpus",words[10],words,20))
    print(cluster.read_cluster_sentence("./cluster",words[10]))
    
test_d2c()