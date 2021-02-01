# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:41:26 2021

@author: luyishen
"""
from pandas import Series, DataFrame

data = {'语文': [68, 95, 98, 90, 80], '数学': [65, 76, 86, 88, 90], '英语':[30, 98, 88,77,90]}

df = DataFrame(data, index = ['张飞', '关羽', '刘备', '典韦', '许褚'], columns = ['语文', '数学', '英语'])

print(df.describe())

df['总分'] = df.apply(lambda x: x.sum(), axis = 1)

df = df.sort_values('总分', ascending=False)

print(df)

