# coding=utf-8

import codecs
import jieba.posseg as pseg
from rank_bm25 import BM25L as BM25

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# 构建停用词表
stopwords = codecs.open(os.path.join(dir_path, 'cn_stopwords.txt'),'r',encoding='utf8').readlines()
stopwords = [ w.strip() for w in stopwords ]

# jieba里的停用词属性
stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']

# 对文字去停用词
def tokenization(text):
    result = []
    words = pseg.cut(text)
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result

# 文档获取类
class CORPUS_RANK(object):
    def __init__(self, corpus):
        self.tokenized_corpus = [tokenization(doc) for doc in corpus]
        self.bm25 = BM25(self.tokenized_corpus)

    def get_document(self, query):
        tokenized_query = tokenization(query)
        doc_scores = list(self.bm25.get_scores(tokenized_query))
        #print(doc_scores)
        return sorted(enumerate(doc_scores), key=lambda item: item[1], reverse=True)
