# -*- coding: UTF-8 -*-

from gensim.models.doc2vec import Doc2Vec
from jieba import lcut
import numpy as np
import cPickle as pickle

# load corpus
with open('news_sohu_test.cor','r')as f:
    txt=f.read()
news_list=txt.split()

# load model
model_DBOW=Doc2Vec.load('model_DBOW_60_8_10')

# generate vectors
for i in range(0,len(news_list)):
    temp=lcut(news_list[i])
    news_list[i]=model_DBOW.infer_vector(temp)
fpic=file('doc_vector.pkl','w')
pickle.dump(news_list,fpic)


