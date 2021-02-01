# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:02:40 2021

@author: luyishen
"""

import pandas as pd


#数据加载
df = pd.read_csv('car_complain.csv')



#数据处理
df = df.drop('problem', axis = 1).join(df.problem.str.get_dummies(','))

#数据分析

#数据清理
def clean(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x

df['brand'] = df['brand'].apply(clean)

#根据品牌分类统计
res = df.groupby(['brand'])['id'].agg(['count'])

tags = df.columns[7 :]

res2 = df.groupby(['brand'])[tags].agg(['sum'])

#merge两个DF
res2 = res.merge(res2, left_index = True, right_index = True, how = 'left')

res2.reset_index(inplace = True)

res2.to_csv("./result.csv")

#按照投诉数量排序
res2 = res2.sort_values('count', ascending = False)

print(res2)


