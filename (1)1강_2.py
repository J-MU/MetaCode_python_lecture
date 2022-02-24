# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 12:18:05 2022

@author: Uk
"""

a=int(3)
b=4         #그냥 int정수 사용하고싶을때는 int() 생략해도 됨
c=float(2)
d=2.0       # x.xxx형태로 대입하면 float()로 인지함

# 정수와 실수의 덧셈 뺄셈의 결과는 실수
e=a+c
f=a-c
g=a*c
h=c/d

# 산술 연산자
# a//b : a를 b로 나눈 몫
4//3

# a%b  : a를 b로 나눈 나머지
4%3
# a ** b : a의 b승
4**3

#Boolean( 참/ 거짓)
#비교연산자의 결과는 Boolean으로 참(True)와 거짓(False)로 나타낸다.
3>4
3<4
3==4
3!=4

#복합 대입 연산자
a=3
a=a+2
print(a)

a=3
a+=2
print(a)

# 문자열(String)
#파이썬은 따옴표'' 와 쌍따옴표 "" 둘다 사용 가능하다 하지만 쌍으로 사용해야 한다
a='thank'
b="you"
# 따옴표 하나와 쌍따옴표 하나로는 안된다.
c='thank"
#따옴표 3개씩으로 둘러싸면 장문의 문자열, 줄바꿈도 쉽다.
d="""t
h
a
n
k
s
"""
e="""이상훈이 말했습니다. "안녕하세요" """

#문자열 끼리의 합
a+b
a+" "+ b

#문자열에 숫자를 곱하면 그 숫자만큼 반복
a*2

#문자열에 변수를 사용하는 방법은 .format()을 활용한다.
#사용법은 문자열 안의 {} 가 변수이고, 스트링 마지막에 .format()을 사용한다.
#변수를 넣는다.
a='이상훈'
name1="{}".format(a)
print(name1)

name='이상훈'
email="alsdnrdl001@gmail.com"
print('{}의 이메일 주소는 {}입니다.'.format(name,email))

#문자열(String)관련 주요 메소드
# split : 특정 문자 또는 빈칸으로 쪼개준다.
#결과는 리스트(list)로 나오는데 다음 강의에서 배운다.
s = "2021-06-01"
result=s.split('-')
print(result)

s="안녕하세요. 제 이름은 이상훈 입니다."
result=s.split(' ')
print(result)

# join : split과 반대 메소드로 생각할 수 있다
# 사용 방법은 "문자열".join(리스트 or 튜플)

result2=' '.join(result)
print(result2)

# upper() : 모두 대문자로
email.upper()

# lower() : 모두 소문자로
email.lower()

# capitalize : 문자열의 첫 글자만 대문자, 나머지는 소문자
email.capitalize()

ex=s.center(50)
ex_1=s.center(50,'*')
ex_2=s.center(50,'/')


s.count('이상훈')

s.find('이상훈')

ex.strip()
ex_1.strip('*')


"asdf123".isalnum()
"Aaaa".isalpha()

"3121231234".isdecimal()
"1113".isdigit()

#음수는?
"-1111".isdecimal() # '-'를 문자로 인식해서 숫자가 아니라고 뜬다.

# 아래와 같은 함수를 만들어서 사용해볼수 있다.
def is_decimal(data):
    try:
        temporary=float(data)
        return True
    except:
        return False

is_decimal("-1111")
is_decimal("1111")

# 식별자 체크 : 식별자란 ? : 변수의 이름, 함수의 이름 등등으로 사용할 수 있는가?
"a".isidentifier()

# 어렵게 생각하지 말고 문자로 시작, 빈칸이 없어야 한다!
"31".isidentifier()
"31a".isidentifier()
"a31".isidentifier()
"a a".isidentifier()
"a_a".isidentifier()


" ".isspace()
print("")
print(" ")

a=""
b=" "
# 둘의 차이는?
len(a)
len(b)

# 과제(1)
# x=5.0 y=3 을 입력하고, 결과창으로
# "x+y=8.0 입니다"를 출력하는 함수 작성
def print_xplusy(x,y):
    print("x+y={} 입니다.".format(x+y))
    return True

print_xplusy(5.0, 3)

# 과제(2)
# x="than3k"
# y="yo97u"
# x와 y를 위와 같이 선언한 후에, 강의에서 학습한 함수를 사용하여 "thank you"를 출력하여라

x="than3k"
y="yo97u"

x=x.replace("3", "") 

y=y.replace("9", "")
y=y.replace("7", "")

str=x+" "+y
print(str)
    

