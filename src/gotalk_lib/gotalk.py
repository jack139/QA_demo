# coding=utf-8

import urllib3
import json, re
from datetime import datetime
from gotalk_lib.bm25 import CORPUS_RANK
from gotalk_lib.knowledge import corpus

urllib3.disable_warnings()

# 调用 gotalk的网络参数
pool = urllib3.PoolManager(num_pools=2, timeout=180, retries=False)

host = 'http://127.0.0.1:8000'
url = host+'/qa'

# 清除文本中非中文非英文的字符（例如：日文、阿拉伯文）
def cleantxt(raw):
    fil = re.compile(u'[^0-9a-zA-Z\u4e00-\u9fa5.，,。？?“”"()（）$￥%!！:：、/|]+', re.UNICODE)
    return fil.sub(' ', raw) 


# 初始化文档获取类
corpus_rank = CORPUS_RANK(corpus)


# 调用go的问答服务
def qa(question):

    question = cleantxt(question)

    # BM25 获取相关文本
    max_index = corpus_rank.get_document(question)

    print(max_index)

    for index, value in max_index[:3]: # 只做3次尝试
        if value==0: # bm25 score是0
            print('Question: ', question, '\n ---> 未找到答案')
            break

        print(index)
        context = cleantxt(corpus[index])

        # 调用参数
        body = {
            'c'  : context,
            'q'  : question,
        }
        #print(body)
        body = json.dumps(body)

        # 调用gotalk
        start_time = datetime.now()
        r = pool.urlopen('POST', url, body=body)
        print('[Time taken: {!s}]'.format(datetime.now() - start_time))

        print(r.status)
        if r.status!=200:
            print(r.data)
            break

        ret = json.loads(r.data.decode('utf-8'))
        if ret['code']=='0':
            if ret['data']!='':
                return ret['data'].replace("##", "") # 英文token会带##
            else:
                continue
        else:
            print('FAIL:', ret['code'], ret['msg'])
            break

    return None

            
# 调用go的问答服务
def qa_with_knowledge(context, question):

    question = cleantxt(question)

    # 调用参数
    body = {
        'c'  : context,
        'q'  : question,
    }
    #print(body)
    body = json.dumps(body)

    # 调用gotalk
    start_time = datetime.now()
    r = pool.urlopen('POST', url, body=body)
    print('[Time taken: {!s}]'.format(datetime.now() - start_time))

    print(r.status)
    if r.status!=200:
        print(r.data)
    else:
        ret = json.loads(r.data.decode('utf-8'))
        if ret['code']=='0':
            if ret['data']!='':
                return ret['data'].replace("##", "") # 英文token会带##
        else:
            print('FAIL:', ret['code'], ret['msg'])

    return None

            
