#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    脚本名: 数据获取
Created on 2018-07-11
@author:David Yisun
@group:data
@contact:davidhu@wezhuiyi.com
"""
import sys
sys.path.append('../')
from utils import question_get, request_data
import datetime
import json
import codecs

def get_result(question):
    ques = question
    no_res = []
    res = []
    step = 0
    for i, q in enumerate(ques):
        if step % 200 == 0:
            print('It is request for the question: {0}'.format(q))
        step += 1
        try:
            data = request_data.get_stock_info(q)
            t = datetime.datetime.now().strftime('%Y-%m-%d')
            _stock = [[j[0], j[1]] for j in data['data']]
            stock = _stock if len(_stock) < 15 else _stock[0:15]
        except:
            no_res.append(q)
            continue
        if stock == []:
            no_res.append(q)
            continue
        _res = [q, stock, t]
        res.append(_res)
    return no_res, res
if __name__ == '__main__':
    no_res = question_get.get_question()
    data = []
    for i in range(20):
        no_res, _data = get_result(no_res)
        data = data+_data
        if no_res == []:
            break
    result = {'data': data}
    file = json.dumps(result)
    with codecs.open('../result/data.txt', 'w', 'utf8') as f:
        f.write(file)
    with codecs.open('../result/no_result.txt', 'utf8') as f:
        f.write('/n'.join(no_res))