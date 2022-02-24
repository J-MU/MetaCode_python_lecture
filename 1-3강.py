# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:29:34 2022

@author: Uk
"""

score=30

if score<30:
    print("fail")

elif score >= 30:
    print("pass")

else :
    print("error")

score=90

if score>60:
    print("pass") #여기서 끝 나버
elif score>80:
    print("great")
    
    
score=90
if score>60:
    print("pass")

if score>80:
    print("Summa Cum")
    
for i in range(5):
    print(i)
    
for i in [0,1,2,3,4]:
    print(i)
    
for i in ['apple','bannana','cherry']:
    print(i)
    
# while구문

i=0
while i<10:
    print(i)
    i+=1

# break, continue

while True:
    input_data=input("정수의 짝/홀을 알려드립니다. \n 종료하시려면 .을 눌러주세요")
    if not input_data.isnumeric():
        break
    
    elif int(input_data) % 2 ==0:
        print("{}는 짝수입니다".format(input_data))

    elif int(input_data) % 2 ==1:
        print("{}는 홀수입니다".format(input_data))
        

# 리스트와 반복문
name={'이정재','박해수','오영수',"위하준","정호연","허성태"}
for i in name:
    print(i)

# 인덱스의 위치도 알려주는 enumerate()
for i,j in enumerate(name):
    print(i,j)    
    
# 리스트에서는 리스트 속 데이터에서 조건에 맞는 데이터를 가져오는 다른 방법이 있다.
# 약속된 구문으로 숙지하자
lst=list(range(9))
lst_odd=[x for x in range(9) if x%2==1]
lst_even=[x for x in lst if x%2==0]    
print(lst_odd)
print(lst_even)

# 과제
# 아래 list를 a라는 dictionary에 1번: 이정재 , 2번: 박해수 식으로 딕셔너리로 만들어 보자.
name={'이정재','박해수','오영수',"위하준","정호연","허성태",'미주령'}
dic_name={}

for i,j in enumerate(name):
    dic_name[str(i)+'번: ']=j
    
print(dic_name)

# 첫번째 방법
a=dict()
b=[]

for i in range(1,len(name)+1):
    b.append("{}번".format(i))

for i in range(0,len(name)):
    a[b[i]]=name[i]
    
# 두번째 방법
a= dict(zip(b,name))
print(a)
