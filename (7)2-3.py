# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 21:04:23 2022

@author: Uk
"""

# 실무에서 가장 많이 사용하는 numpy 라이브러리 함수는
import numpy as np
svae_data = np.zeros((3,3))

#위와 같이 데이터를 저장하기 위한 공간이다.

# array에서 multiply와 dot(내적)의 차이는 아래와 같다.
x=np.array([[2,3],[4,2]])
y=np.array([[1],[2]])

np.multiply(x,y)
np.multiply(y,x)

np.dot(y,x)
np.dot(x,y)

z=np.random.randint(0,100,size=(10,10))
p=np.random.randint(0,100,size=(10,5))

np.multiply(z,p)
np.dot(z,p)

q=np.random.randint(0,100,size=(2,2))
w=np.random.randint(0,100,size=(1,2))

np.dot(q,w)
np.multiply(q,w)

z=np.array([[3,4,5],[4,5,6],[6,7,8],[1,2,3]])

z[[0,1,2],[0,1,2]]

z[z>4]

np.sum(x,axis=0)
np.sum(x,axis=1)

#==========================================================
# shuffle, sampling
#==========================================================

sample_array=np.arange(1,100)

# shuffle은 원본 자체를 바꾸고
np.random.shuffle(sample_array)

#permutation은 원본은 그대로이며 랜덤하게 순서를 바꾼 객체를 반환한다.
a=np.random.permutation(sample_array)

np.random.choice(sample_Array,200,replace=False) #replace는 중복 허용
np.random.choice(sample_array,200,replace=True)

np.random.seed(76923)
np.random.choice(sample_array,5,replace=True)

np.random.randint(99,size=5)


# 과제
# 아래 배열에서 두번째 행중에서 5이상인 숫자의 배열만 선택하시오
x=np.array([[1,2,3],[4,5,6],[7,8,9]])

#답안
x[1][x[1]>5]
