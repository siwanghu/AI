# -*- coding: utf-8 -*-
from AIFish.nlp import nlp,train,tuling

def test_nlp():
    print("语料库训练")
    print(train.idf("./corpus",41780))
    print(nlp.idf("./corpus","价格"))
    print(nlp.tf("我看到你们网站有个免费试用是吧"))
    print(nlp.cut_word("我看到你们网站有个免费试用是吧"))
    print(nlp.word_posseg("我看到你们网站有个免费试用是吧"))
    print(nlp.word_frequency("./corpus","./stopword"))
    print(nlp.extract_keyword("我看到你们网站有个免费试用是吧","./corpus"))
    print(nlp.draw_WordCloud("./1.png","./corpus","./stopword"))
    print(tuling.get_response("今天天气怎么样"))

test_nlp()