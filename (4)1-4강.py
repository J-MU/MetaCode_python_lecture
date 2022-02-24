# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:40:26 2022

@author: Uk
"""

# ===============================================
#
# 기본 구문
# def 함수이름(매개변수):
#   처리할 로직
#   return 출력값
#
#
# ===============================================

def sum1(a,b):
    return a+b

a=sum1(3,2)

def sum1_1(a,b):
    return a,b,a+b

d,e,f=sum1_1(3,2)
g=sum1_1(3,2)

def sum2(a,b):
    if type(a)==int and type(b)==int:
        return a+b
    else:
        print("숫자를 입력하십시오")
        
sum2(3,2)
sum2("b",2)

# ==============================================================
# 함수의 input으로 여러개의 값을 입력하고 싶은데, 변수를 그만큼 늘려줘야 하는가?
# ===============================================================

def sum3(*args):
    return sum(args), type(args)

sum3(1,2,3,4,5,6,7,8,9,10)

# 굳이 *args로 만들 필요는 없고 문자 앞에 *를 하나 붙이면 된다.
def sum4(*aaaa):
    return sum(aaaa), type(aaaa)

sum4(1,2,3,4,5,6,7,8,9,10)

# 함수를 만들때 하나의 변수 + 튜플을 input으로 받으려면 반드시 순서를 지켜야한다.
def exer(name, *args):
    print(name)
    print(len(args))
    print(type(args))
    
exer("이상훈",1,2,3)

def mean1(**kwargs): # keyword arguments 의 줄임말
    print(type(kwargs))
    return sum(kwargs.values())

mean1(a=1,b=2)

class coin:
    def __init__(self,name):
        self.name=name
        self.shares=0
        
    def buy(self,shares):
        self.shares+=shares
        print(self.name+"코인 {}개 매수 완료".format(shares))
    
    def sell(self,shares):
        self.shares-=shares
        print(self.name+"코인 {}개 매도 완료".format(shares))
        
    def balance(self):
        print(self.name+"코인은 {}개 보유중입니다.".format(self.shares))
        
eos=coin("EOS")
eos.buy(3)

eos.balance()

eth=coin("ETH")
eth.buy(5)
eth.buy(4)
eth.buy(3)
eth.sell(7)
eth.balance()

# *args는 튜플로 받아지고, 튜플은 수정이 불가능하기 때문에 리스트로 바꿔서 생각한다.

class squid_game:
    def __init__(self,*args):
        self.data=list(args)[0]
        print("참가자 명단은 아래와 같습니다. \n"+str(self.data))

    def check(self):
        print(self.data)
        print(type(self.data))
        
        return self.data
    
    def fail(self,*args):
        self.data=[x for x in self.data if x not in list(args)]
        print(args)
        print(type(self.data))
        return self.data
    
    def fail2(self,*args):
        args=list(args)[0]
        print(len(args))
        for i in range(0,len(args)):
            print(args[i])
            self.data.remove(args[i])
            
        return self.data
    
    def night_random_fight(self,num):
        for i in range(num):
            j=self.data.pop()
            print("{} 번째 참가자 사망".format(j))
        return self.data
    
first_list=list(range(1,51))
first_comp=squid_game(first_list)

a=first_comp.check()
import random
first_dead_list=random.sample(first_list,10)

first_live_list=first_comp.fail(first_dead_list)

second_dead_list=random.sample(first_live_list,10)
second_comp=squid_game(first_live_list)
second_live_list=second_comp.fail2(second_dead_list)

# 과제

# 계산기 만들기
# 클래스 + 함수 강의에서 무조건 나오는 과제
# class 명은 cal, 덧셈함수 add, 뺄셈함수 sub 두개만 만들어보기

class cal:
    def __init__(self):
        self.num=0
        print(self.num)
        
    def add(self,number):
        self.num+=number
        print("현재 값은{}입니다.".format(self.num))
        return self.num
    def sub(self,number):
        self.num-=number
        print("현재 값은{}입니다.".format(self.num))
        return self.num
    
calculator=cal()
calculator.add(3)
calculator.add(5)
calculator.sub(2)
