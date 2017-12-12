# -*- coding: UTF-8 -*-

import cPickle as pickle
import random

# eucilean distance(squared)
def eucilean(a,b):
    dis=0
    for i in range(0,len(a)):
        dis+=(a[i]-b[i])*(a[i]-b[i])
    return dis

# load doc vector
f=file('doc_vector.pkl','r')
doc_vec=pickle.load(f)

# 从某一篇文章出发，寻找主题最相近的文本
# 也可自己输入文本并生成向量，查找相似文本
in_id=random.randint(0,700)
in_vec=doc_vec[in_id]

# generate distance vector and find the nearest doc
doc_dis=[]
for vec in doc_vec:
    doc_dis.append(eucilean(vec,in_vec))
doc_dis[in_id]=1000
out_id=doc_dis.index(min(doc_dis))

# check the performance
with open('news_sohu_test.cor','r')as f:
    txt=f.read()
news_list=txt.split()
print 'original:###'+news_list[in_id]
print 'similar:###'+news_list[out_id]
