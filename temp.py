# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
 
data = pd.read_csv('D:/report.csv') 
l1 = int(input("您在意的條件(1.價格2.房間坪數3.住宿品質4.與靜宜距離):")) 
if l1 == 1: 
    q=data.sort_values(by=['價格']) 
elif l1 == 2: 
    q=data.sort_values(by=['房間坪數'],ascending=False) 
elif l1 == 3: 
    q=data.sort_values(by=['住宿品質'],ascending=False) 
elif l1 == 4: 
    q=data.sort_values(by=['與靜宜距離'])     
else : 
    print("請重新啟用程式，選擇您在意的條件") 
print(q[:5])

import pandas as pd 
 
data = pd.read_csv('D:/report.csv') 
data['ps']=0     
for i in range(len(data)): 
    if (data.iloc[i,2]<3000 or data.iloc[i,2]>20000): 
        data.iloc[i,9]=0 
    else: 
        data.iloc[i,9]=100-((data.iloc[i,2])/500) 
data['ss']=0     
for j in range(len(data)): 
    if (data.iloc[j,1]<4): 
        data.iloc[j,10]=0 
    elif(data.iloc[j,1]>=20): 
        data.iloc[j,10]=100     
    else: 
        data.iloc[j,10]=80+(data.iloc[j,1]) 
data['qs']=0     
for k in range(len(data)): 
    if (data.iloc[k,7]>4): 
        data.iloc[k,11]=100 
    else: 
        data.iloc[k,11]=100-(((5-data.iloc[k,7]))*20) 
data['as']=0     
for m in range(len(data)): 
    if (data.iloc[m,8]<300): 
        data.iloc[m,12]=100 
    elif (data.iloc[m,8]>1000): 
        data.iloc[m,12]=0 
    else: 
        data.iloc[m,12]=100-((data.iloc[m,8])/100) 
 
 
size = float(input('請輸入房間坪數的比重:')) 
if size < 0 : 
    print('比重不可小於0，請重新輸入房間坪數的比重:') 
    size = float(input('請輸入房間坪數的比重:')) 
price = float(input('請輸入價格的比重:'))     
if price < 0 : 
    print('比重不可小於0，請重新輸入價格的比重:') 
    price = float(input('請輸入價格的比重:')) 
quality = float(input('請輸入住宿品質的比重:')) 
if quality < 0 : 
    print('比重不可小於0，請重新輸入住宿品質的比重:') 
    quality = float(input('請輸入住宿品質的比重:')) 
away = float(input('請輸入與靜宜距離的比重:')) 
if away < 0 : 
    print('比重不可小於0，請重新輸入與靜宜距離的比重:') 
    away = float(input('請輸入與靜宜距離的比重:')) 
total = size + price + quality + away 
while int(total) != 100: 
    size = 0 
    price = 0 
    quality = 0 
    away = 0 
    print('比重總和超過100%，請重新輸入您評估的條件比重') 
    size = float(input('請輸入房間坪數的比重:')) 
    if size < 0 : 
        print('比重不可小於0，請重新輸入房間坪數的比重:') 
        size = float(input('請輸入房間坪數的比重:')) 
    price = float(input('請輸入價格的比重:'))     
    if price < 0 : 
        print('比重不可小於0，請重新輸入價格的比重:') 
        price = float(input('請輸入價格的比重:')) 
    quality = float(input('請輸入住宿品質的比重:')) 
    if quality < 0 : 
        print('比重不可小於0，請重新輸入住宿品質的比重:') 
        quality = float(input('請輸入住宿品質的比重:')) 
    away = float(input('請輸入與靜宜距離的比重:')) 
    if away < 0 : 
        print('比重不可小於0，請重新輸入與靜宜距離的比重:') 
        away = float(input('請輸入與靜宜距離的比重:')) 
    total = size*10 + price*10 + quality*10 + away*10 
else: 
    data['s'] = data['ss']*size/100 + data['ps']*price/100 + data['qs']*quality/100 + data['as']*away/100 
    data_score_sort=data.sort_values(by=['s'],ascending=False) 
    top10_data_ss=data_score_sort[:5] 
    print(top10_data_ss[['宿舍名稱或地址']+['房間坪數']+['價格']+['房型']+['電費']+['住宿品質']+['與靜宜距離']])
import pandas as pd 
import numpy as np 
data = pd.read_csv('D:/report.csv') 
#a=np.array(data)     
rp = [] 
roomprice = int(input("期望的房間月租:")) 
 
rp.append(data[data['價格']<=roomprice] ) 
 
     
 
rp=pd.DataFrame(np.concatenate(rp)) 
        
 
rs=[] 
roomsize = input("期望的房間大小:") 
rs.append(rp[rp[1]>=int(roomsize)]) 
rs=pd.DataFrame(np.concatenate(rs)) 
       
 
rq=[] 
roomququality = input("期望的房間品質(1-5分，5分最高):") 
   
rq.append(rs[rs[7]>=int(roomququality)]) 
rq=pd.DataFrame(np.concatenate(rq)) 
         
 
rw=[] 
roomway = input("期望房間離靜宜大學的距離(以公尺為單位):") 
     
rw.append(rq[rq[8]<=int(roomway)]) 
     
list3_result=pd.DataFrame(np.concatenate(rw)) 
     
  
if len(list3_result) == 0: 
    print('非常抱歉，沒有適合您的房間') 
else: 
    print(list3_result)    
    