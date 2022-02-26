# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 20:14:58 2022

@author: Uk
"""
f=open('coin.txt','r',encoding='utf8')
line=f.readlines()
f.close()

#콤마를 구분으로 쪼갠다
result=line[0].split(',')

#리스트 안의 string을 float로 바꿔주는 방법1
result=list(map(float,result))

#리스트 안의 string을 float로 바꿔주는 방법2
result=[float(x) for x in result]

#위 두가지 모두 "" 빈칸 때문에 작동이 안된다.
#for문을 사용해 하나씩 바꿔본다
for i in range(len(result)):
    result[i]=float(result[i])
    print(i,result[i],type(result[i]))

#trv & except
for i in range(len(result)):
    try:
        result[i]=float(result[i])
        print(i,result[i],type(result[i]))
    except:
        print("리스트 {}번째에서 error 발생, 다음으로 넘어갑니다.".format(i))

print(result)

result=[8,9,10,"",11,12,"",13]

# 각 원소의 타입은 ?
for i in result:
    print(type(i))
    
# pass, continue, raise error

for i in result:
    if i> 10 :   # ""은 10과 대소비교가 되지않아 에러가 뜸
        print(i)

# Try & except
for i in result:
    try:
        if i> 10:
            print(i)
    except:
        print("대소 비교 불가")
        
for i in result:
    try:
        if i> 10 :
            if i==11:
                print("11발견")
                pass
            print(i)
    except:
        print("대소비교 불가")
        continue
    
for i in result:
    try:
        if i> 10 :
            if i==11:
                print("11발견")
                continue
            print(i)
    except:
        print("대소비교 불가")
      
for i in result:
    try:
        if i>10:
            if i==11:
                print("11발견")
                raise Exception("에러")
            print(i)
    except Exception as e:
        print(e)
        
# 과제
# 예외처리 구문에서 pass와 continue의 차이점을 서술하시오

'''
    continue는 다음 반복구문으로 넘어가는 역할을 한다.
    
    pass의 경우 아무런 역할도 하지 않는다.
    다만 이런경우 역할이 있다고 할 수 있겠다.
    
    class Temp():
        def function():
            pass
        
    위의 코드에서 function()이 아무런 역할을 하지 않을 수 있다.
    다른 메소드를 먼저 구현후 차후에 구현하려는 목적이거나
    부모 클래스에선 아무런 역할을 하지않는 function을 작업해놓고
    자식클래스가 상속받으면서 function을 구현하려 할 수 있기 때문이다.
    허나 function을 아애 비워놓을 경우 error가 발생하므로 pass를 써놓는다.
    
    추가로 예외가 발생했을 때 그냥 넘어간다는 의미로도 사용된다.
    def divide(x,y):
        z=None
        try:
            z=x/y
        except:
            pass
        return z
    
    divide(6,0)
    
    위 코드에서 y가 0일경우 error가 발생하지만
    except에서 어떠한 action도 취하지 않고 넘어가고싶을때 pass로 나타낸다.
'''