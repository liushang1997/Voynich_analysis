from gensim.models import word2vec
import numpy as np
import os
import re

if os.path.exists('db.model'):
    model = word2vec.Word2Vec.load("db.model")
else:
    sentences = word2vec.Text8Corpus("VM_clean_para")  # 加载语料
    model = word2vec.Word2Vec(sentences, size=15, sg=1, min_count=5, workers=8, alpha=0.001, hs=0, window=10,
                              iter=1000, batch_words=1000)
    model.save("db.model")

# 获取“学习”的词向量
print('?:' + str(model['?']) + str(type(model['?'])))
# # 计算两个词的相似度/相关程度
y1 = model.similarity("or", "ar")
print(y1)
# # 计算某个词的相关词列表
y2 = model.most_similar("or", topn=10000)  # 20个最相关的
print(y2)

word_list = []
for j in range(len(y2)):
    word_list.append(y2[j][0])
print(word_list)

# # 寻找对应关系
# print("书-不错，质量-")
# y3 = model.most_similar(['ar', 'or'], ['do'], topn=3)
# print(y3)
# # 寻找不合群的词
# y4 = model.doesnt_match("书 书籍 教材 很".split())

# f = open('VM_word_dic')
# VM_word = f.read()
# VM_word_dic = re.split(r'\n', VM_word)
# del VM_word_dic[-1]

vec_array = np.zeros((len(word_list), 15))

for i in range(len(word_list)):
    vec_array[i] = model[word_list[i]]

print(vec_array, vec_array.shape)

np.save('vec_array.npy', vec_array)
