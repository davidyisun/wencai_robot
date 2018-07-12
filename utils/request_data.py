#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    脚本名: 请求数据
Created on 2018-07-12
@author:David Yisun
@group:data
@contact:davidhu@wezhuiyi.com
"""
import requests
import json
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
headers = {"Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Connection":"keep-alive",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
           "Cookie":"searchGuide=sg; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1519443379,1521098974; user=MDpqdW5yZW41MDI2OjpOb25lOjUwMDozOTc3MzA3NDg6NywxMTExMTExMTExMSw0MDs0NCwxMSw0MDs2LDEsNDA7NSwxLDQwOjI3Ojo6Mzg3NzMwNzQ4OjE1MjEwOTg5NzM6OjoxNDkxMDQzNDQwOjYwNDgwMDowOjE3ZjNiYzgwYWRkYmMxMWVhOGVhYzMwYjRlMjFlMmYzOTpkZWZhdWx0XzI6MA%3D%3D; userid=387730748; u_name=junren5026; escapename=junren5026; ticket=cb622e15de1acf0a4042475ddb9ad3cc; __utma=156575163.1411408120.1515675977.1518146740.1521099880.4; __utmz=156575163.1521099880.4.4.utmcsr=10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/; PHPSESSID=dac2981ded872040d18847abbf133f51; cid=dac2981ded872040d18847abbf133f511521447252; ComputerID=dac2981ded872040d18847abbf133f511521447252; other_uid=Ths_iwencai_Xuangu_41c74e0a596c06249f47785b755a4672; v=Ahq680tRFLoxeJgWJfKQEX15a8s4S5-sEM8S1SSTxq14l7R9DNvuNeBfYtf3"}


url1 = 'https://www.iwencai.com/data-robot/get-fusion-data'  # method: post

url_info = 'https://www.iwencai.com/stockpick/cache?token={0}&p=1&perpage=70&changeperpage=1'  # method: get


def get_token(question=''):
    parameters = {'w': question}
    token = -1
    for i in [1, 2, 3]:
        res = requests.post(headers=headers, url=url1, data=parameters)
        info = json.loads(res.text)
        token = info['data']['wencai_data']['result']['token']
        if token != '':
            return token
    return token

def get_stock_info(question=''):
    token = get_token(question=question)
    url = url_info.format(token)
    res = requests.get(headers=headers, url=url)
    info = json.loads(res.text)
    title = info['title']
    data = info['result']
    res = {'title': title,
           'data': data}
    return res


if __name__ == '__main__':
    qes = '市盈率'
    get_stock_info(qes)
    pass