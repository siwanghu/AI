# -*- coding: utf-8 -*-
from AIFish.w2v import word2vec

def test_v2c():
    print(word2vec.train("./word2vec",["、","，","\n","访客"]))
    print(word2vec.vector("./word2vec","价格"))
    print(word2vec.similar_word("./word2vec","价格"))
    print(word2vec.similar_only_word("./word2vec","价格"))

test_v2c()