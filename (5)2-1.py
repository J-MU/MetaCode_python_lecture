# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 19:33:37 2022

@author: Uk
"""

f=open('test.txt','r',encoding='utf8')
line=f.readlines()
f.close()

f=open('정보.txt','r',encoding='utf8')
line=f.readlines()
f.close()

print(line)

for i in range(len(line)):
    line[i]=line[i].replace('\n', '')

print(line)

# list의 각 원소의 : 로 구분해보자
# 결과 [['이름','이상훈'],[지역,대구],[나이,24]]

f=open('정보.txt','r',encoding='utf8')
line=f.readlines()
print(line)
for i in range(len(line)):
    line[i]=line[i].replace('\n', '')
print(line)


tmp=list()

for i in range(len(line)):
    tmp.append(line[i].split(':'))
    
print(tmp)

f=open('정보.txt','r',encoding='utf8')
line=f.readlines()
print(line)
for i in range(len(line)):
    line[i]=line[i].replace('\n', '')
print(line)

tmp=list()

for i in range(len(line)):
    tmp.extend(line[i].split(':'))
print(tmp)
