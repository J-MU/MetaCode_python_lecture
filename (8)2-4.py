# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 21:28:18 2022

@author: Uk
"""

# ========================================================
# pandas 라이브러리
# 시리즈 : 한줄짜리.
# =========================================================

import pandas as pd
example=pd.Series() # 시리즈의 S는 대문자여야함.

# 시리즈를 만드는 법 1. 리스트를 활용
lst=[1,2,3,4,5]
ex_1=pd.Series(lst)
print(ex_1,type(ex_1))

# 시리즈의 loc, iloc 인덱싱
ex_1.loc[0]
ex_1.iloc[0]

dictionary={"성별":"남자","이름":"정민욱","지역":"대구","나이":"24"}
ex_2=pd.Series(dictionary)
print(ex_2)

ex_2.loc[1]
ex_2.iloc[1]
ex_2.loc['이름']

# 딕셔너리 형태를 시리즈로 만들면 key가 인덱스로 지정된다.
# 인덱스로 지정된 딕셔너리의 key를 데이터로 빼내는 방법은 reset_index()함수이다.
ex_2.reset_index(drop=True)
ex_2.reset_index(drop=False)
ex_2.reset_index() #drop=false 가 default 값
ex_3=ex_2.reset_index()

print(ex_3)
ex_3.loc[3,0]
ex_3.loc[3,'index']
ex_3.iloc[3,0]
ex_3.iloc[3,1]

ex_3.shape
type(ex_3)

lst_4=[[1,2,3,4,5],[1,2,3,4,5]]
ex_4=pd.Series(lst_4)

# ==========================================================
# 데이터 프레임
# 가장 많이 사용하는 함수
# ==========================================================

import numpy as np
import pandas as pd

#array -> data frame
array=np.array([(3,2,31),(4,14,7)])
ex_1=pd.DataFrame(array)

dictionary={"성별":"남자","이름":"정민욱","지역":"대구","나이":"24"}
ex_2=pd.DataFrame([dictionary])
ex_3=pd.DataFrame(dictionary,index=['1'])

# 0으로만 이루어진 4*4 데이터 프레임을 만드는 방법은?

pd.DataFrame(np.zeros((4,4)))


