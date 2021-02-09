# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:32:11 2021

@author: luyishen
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd 


# 得到页面的内容

def get_page_content(request_url):
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10)
    content = html.text
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup

def analysis(soup):
    df = pd.DataFrame(columns = ['id', 'brand, model', 'type', 'des', 'problem', 'datetime', 'status'])
    temp = soup.find('div', class_ = 'tslb_b')
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            id, brand, model, type, des, problem, datetime, status = td_list[0].text, td_list[1].text, \
                td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text
            temp = {}
            temp['id'] = id
            temp['brand'] = brand
            temp['model'] = model
            temp['type'] = type
            temp['des'] = des
            temp['problem'] = problem
            temp['datetime'] = datetime
            temp['status'] = status
            
            df = df.append(temp, ignore_index = True)
    return df

result = pd.DataFrame(columns = ['id', 'brand, model', 'type', 'des', 'problem', 'datetime', 'status'])
url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
pages = 20
for i in range(pages):
    request_url = url + str(i+1) + '.shtml'
    soup = get_page_content(request_url)
    df = analysis(soup)
    result = result.append(df)
    
result.to_excel('car_complain.xlsx', index=False)
    