#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    脚本名: 问句整理
Created on 2018-07-11
@author:David Yisun
@group:data
@contact:davidhu@wezhuiyi.com
"""
import codecs
import pandas as pd
import itertools

# 获取形态关键词
def _get_forms():
    forms = pd.read_table('../data/forms.txt', sep='\t', encoding='utf8')
    forms.columns = ['form']
    return forms


# 获取指标关键词
def _get_indicators():
    indicators = pd.read_table('../data/indicators.txt', sep=' ', encoding='utf8')
    indicators.columns = ['indicator', 'threshold']
    return indicators


# 获取时间
def _get_time():
    t = ['2017年',
         '2017年上半年', '2017年下半年',
         '上半年', '下半年',
         '2017年一季度', '2017年二季度', '2017年3季度', '2017年4季度',
         '一季度', '二季度', '3季度', '4季度',
         '2017年一月', '2017年二月', '2017年11月', '2017年12月',
         '一月', '二月', '11月', '12月',
         '二月二十四日', '二月二十五日',
         '11月1日', '12月3日',
         '1日', '2日', '3日', '二十四日', '二十五日', '二十六日',
         '2017年11月1日', '2017年11月2日', '2017年11月3日']
    times = pd.DataFrame(t)
    times.columns = ['time']
    return times


# 形成问句
def get_question():
    forms = _get_forms()
    indicators = _get_indicators()
    times = _get_time()
    times['key'] = 1
    # 单指标
    q_indicators = []
    q_indicators = q_indicators+indicators['indicator'].drop_duplicates().tolist()
    ind_thr = pd.DataFrame(indicators['indicator']+indicators['threshold'])
    q_indicators = q_indicators+ind_thr[0].tolist()
    ind_thr['key'] = 1
    t_i_t = pd.merge(times, ind_thr, on=['key'], how='outer')
    time_ind_thr = t_i_t['time']+t_i_t[0]
    q_indicators = q_indicators+time_ind_thr.tolist()
    # 单形态
    q_forms = []
    q_forms = q_forms+forms['form'].tolist()
    forms['key'] = 1
    t_f = pd.merge(times, forms, on=['key'], how='outer')
    time_form = t_f['time']+t_f['form']
    q_forms = q_forms+time_form.tolist()
    # 组合 指标+形态
    together_list = q_indicators+q_forms
    groups = []
    for i in itertools.combinations(together_list, 2):
        q = i[0]+i[1]
        groups.append(q)
    res = []
    res = res + q_indicators + q_forms
    return res


if __name__ == '__main__':
    print(get_question())
    pass
