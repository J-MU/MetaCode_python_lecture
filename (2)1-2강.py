# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:00:43 2022

@author: Uk
"""

# 시작은 항상 0부터

score=[85,90,80,75,95]
score[0]
score[1]
score[2]
score[3]
score[4]

score[-1]
score[-5]

# list[n:m]으로 리스트 전체중 일부만 추출할 수 있으며 n번째 포함 m번째 미포함이다.
score[1:2] # 90
score[1:3] # 90 80

# 시작하는 n을 생략하여 0번째부터 m번째 미포함까지
score[:3] # 85 90 80

# 끝나는 m도 생략가능 2번째부터 끝까지
score[2:] # 80 75 95

# 리스트 뒤에 추가하는 함수 .append()
score.append(100)
print(score)

# 리스트 안에 있는 요소를 지우는 함수 del
del score[5]
print(score)

# 리스트 내용을 범위로 지우는 방법
score[2:]=[]
print(score)

score=[85,90,80,75,95]
# append함수와 비슷하지만, append 함수는 리스트에 리스트 자체로 추가한다.
# extend 함수는 리스트를 추가해도 리스트가 풀리고 요소만 추가한다.
score.append([100,100])
print(score)
score.extend([99,99])
print(score)

# 과제
# 리스트를 다음과 같이 선언한 후에 lst1=[1,2,3,4,5,6,7,8,9,10]
# lst2=[6,7,8,9,10,1,2,3,4,5] 의 결과가 나오도록 한줄 코딩을 해본다

lst1=[1,2,3,4,5,6,7,8,9,10]
lst2=lst1[5:10]
lst2.extend(lst1[0:5])
print(lst2)

# 정답
lst1=[1,2,3,4,5,6,7,8,9,10]
lst2=lst1[5:]+lst1[:5]

# 리스트의 복사
nums=list(range(10)) # 0~9 까지의 정수를 원소로 하는 리스트 생성
nums1=nums            # nums1에 nums를 복사하는것 같지만 사실 같은 객체를 가리키는것
nums2=nums[:]        # 복사

nums[0]="a"

print(nums)
print(nums1)
print(nums2)

# 리스트에서뿐 아니라 이와 같은 상황에서 쓸 수 있는 copy 라이브러리사용
import copy

nums3=copy.deepcopy(nums)
nums[0]="a"
print(nums3)
print(nums)

id(nums)
id(nums1)
id(nums2)
id(nums3)

# ==========================================================
# 튜플, 집합, 딕셔너리
# ==========================================================
# 튜플은 리스트와 비슷하게 데이터 저장을 담당하지만 요소들을 변경할 수 없다

tpl=(0,1,2,3,4,5,6,7,8,9)

tpl[1]
tpl[3:5]

tpl[1]=0 # 변경 불가능 하다.

# 튜플의 용도는 변경이 안되어야 하는 데이터 저장

tpl.count(2) # 튜플 안에2가 몇개가 있는가?
tpl.index(3) # 튜플 안에 3의 위치는?

# ==========================================================
# 
# 집합
# 집합은 {} 를 사용해서 선언하는 자료형으로 중복을 허용하지 않음
# 집합 연산(교집합, 합집합, 차집합, 대칭 차집합) 을 위한 자료형
# 중복된 원소는 하나만 제외하고 모두 무시됨
# 원소의 순서가 의미가 없으므로 인덱싱/슬라이싱 불가
# 순서가 의미 없기 때문에 []로 만들고 순서가 붙는(인덱싱) 리스트는
# 원소에 순서가 있기 때문에 set의 원소가 될 수 없다.
# ==========================================================
 
#집합은 {}를 사용해서 만들 수 있다.
name={'이정재','박해수','오영수',"위하준","정호연","허성태"}
type(name)
#공집합을 만들때는 {}로 하면 딕셔너리가 되므로 set을 이용한다.

name1={}
type(name1)

name2=set()
type(name2)

# 집합안에 원소로 포함되어 있는지 여부 검사
"오영수" in name
"이상훈" in name

names={'이정재',"이정재","박해수"}
len(names)
print(names)

names={'이정재',[1,2]}
# [1,2] 라는 리스트는 순서 0번째 1번째 가 있기 때문에 set이 될 수 없음

# =======================================================
# 원소의 추가
# =======================================================

name={'이정재','박해수','오영수',"위하준","정호연","허성태"}
name.add('압둘 알리')
print(name)

# 여러개의 원소 추가, 리스트, 튜플, 딕셔너리 다 넣을 수 있는데 다 원소로 쪼개져서 저장된다.

name.update([1,2,3,4,5])
print(name)

# =======================================================
# 원소의 추가
# =======================================================
# 1. remove() 함수, 집합에 없는 원소를 지우려 시도하면 에러 발생

 name.remove('이상훈')

# 2. discard()함수, 집합에 없는 원소를 제거하려 시도해도 에러 발생하지 ㅇ낳음
name.discard('이상훈')

# 그렇다면 무조건 remove가 아닌 discard가 좋은 것일까?

# 3. pop()함수는 랜덤하게 요소 제거 후 반환
name.pop()
print(name)

# 4. clear() 공집합으로 만듬
name.clear()
print(name)


# ===================================================
# 집합의 연산
# 합집합: | 또는 union 메소드
# 교집합: & 또는 intersection 메소드
# 차집합: - 또는 difference 메소드 사용
# 대칭 차집합: ^ 또는 symmetric_difference 메소드 사용
# ===================================================

a={1,2,3,4}
type(a)
b=set([3,4,5,6])

# 합집합
a|b
a.union(b)

# 차집합
a-b
b-a
a.difference(b)

#대칭 차집합
a^b
a.symmetric_difference(b)

#========================================================
# 딕셔너리는 key와 value의 매칭으로 구성된다.
# 뒤에서 배울 pandas의 dataframe과 비슷한 구조이다.
# value 에는 하나의 원소가 들어갈 수도 있으며 리스트 등 다양하게 들어갈 수 있다.
#=========================================================

information={"이름": "정민욱" , "나이": 25, "키":"178"}
type(information)

information.items()
information.keys()
information.values()

#KEY가 중복되면 안된다.
information={"이름": "정민욱", "나이":25,"키":178, "이름": "UK"}
information.keys()
information['이름']

# 기존에 있는 key에 해당하는 값 변경
information={"이름": "정민욱" , "나이": 25, "키":"178"}
information["나이"]="24"
information

# 기존에 key가 없다면 새로운 쌍 추가
information['지역']="대구"
information

# GET 함수의 사용. 찾는 KEY에 해당하는 값을 출력. 
# KEY가 없다면 미리 설정해준 출력문자가 출력된다.
information['성별'] # 성별이라는 key가 없다.
information.get('성별') # 에러는 발생 하지 않는다.
information.get('성별','keyerror') #key가 없으니 원하는 출력문자를 설정한다.

#KEY가 있는지 확인하는 방법
type(information.keys())
lst=list(information.keys())
"나이" in lst

"나이" in information # 딕셔너리에서 바로 in을 사용하면 key의 존재 여부를 확인 할 수 있다.


# 과제
# 튜플은 값을 변경할 수 없는 것이 가장 큰 특징이다.
# 하지만 만약 튜플의 값을 변경해야 한다면?
# tpl=(0,1,2,3)을 선언 한 다음, tpl=(0,1,2,3,4)로 수정해본다.
# 힌트는 list를 이용하는 것


tpl=(0,1,2,3)
list1=list(tpl)
print(list1)
list1.append(4)
tpl=tuple(list1)
print(tpl)


# 정답
temp=list(tpl)
temp.append(4)
tpl1=tuple(temp)

