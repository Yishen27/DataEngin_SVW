# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

data = pd.read_csv('./train.csv')

#数据清洗
data['Datetime'] = pd.to_datetime(data.Datetime, format='%d-%m-%Y %H:%M')  
data.index = data.Datetime  
data.drop(['ID', 'Datetime'], axis=1, inplace=True)  
daily_data = data.resample('D').sum()  
daily_data['ds'] = daily_data.index  
daily_data['y'] = daily_data.Count  
daily_data.drop(['Count'], axis=1, inplace=True) 

m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1, daily_seasonality=True)
m.fit(daily_data)  # 拟合
future = m.make_future_dataframe(periods=213)  # 预测未来7个月
forecast = m.predict(future)

m.plot(forecast)
