# 0721 실습



##  1545번_[거꾸로 출력해 보아요](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
num=int(input())
num=list(range(num,-1,-1))
for i in num:
    print(i,end=' ')

```



## 1933번_[간단한 N 의 약수](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
a=int(input())
v=[]
for i in list(range(1,a+1)):
    if a % i ==0:
        v.append(i)
for i in v:
    print(i,end=' ')
```



## 1936번_[1대1 가위바위보](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
a,b=list(map(int,input().split()))
if (a==1) & (b==2):
    print('B')
elif (a==1) & (b==3):
    print('A')
elif (a==2) & (b==1):
    print('A')
elif (a==2) & (b==3):
    print('B')
elif (a==3) & (b==1):
    print('B')
elif (a==3) & (b==2):
    print('A')
else:
    None
```



## 1938번_ [아주 간단한 계산기](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
import math
def cal(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(math.trunc(x/y))
x,y=list(map(int,input().split()))
cal(x,y)

```





## 2019번_[더블더블](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python

n=int(input())
v=[1]
for i in list(range(1,n+1)):
    v.append(2**i)
for i in v:
    print(i, end=' ')
```



## 2025 번_[N줄덧셈](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
a=int(input())
ans=0
for i in list(range(1,a+1)):
    ans+=i
print(ans)
```



## 2027 번_[대각선 출력하기](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
print('#++++\n+#+++\n++#++\n+++#+\n++++#')
```



## 2029 번_[몫과 나머지 출력하기](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python

n=int(input())
v1=[]
v2=[]
for i in list(range(1,n+1)):
    a,b=list(map(int,input().split()))
    print(f'#{i} {divmod(a,b)[0]} {divmod(a,b)[1]}')
```



## 2043 번_[서랍의 비밀번호](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
p,k=list(map(int, input().split()))
print(((abs(p-k)//100)*100) + (((abs(p-k)%100)//10)*10) + ((abs(p-k)%100)%10) + 1)

```



## 2046 번_[스탬프 찍기](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python

a=int(input())
print('#'*a)
```



## 2047 번_[신문 헤드라인](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
a=input()
print(a.upper())
```



## 2050 번_[알파벳을 숫자로 변환](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
txt=input()
for i in list(range(0,len(txt))):
    print(ord(txt[i])-64,end=' ')
```



## 2056 번_[연월일 달력](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
m=int(input())
for i in list(range(1,m+1)):
    n=input()
    if (n[4:6] in ['01','03','05','07','08','10','12']) and ( int(n[-2:])>=1) and (int(n[-2:]) <=31):
        print(f'#{i} {n[:4]}/{n[4:6]}/{n[-2:]}')
    elif (n[4:6] in ['04','06','09','11']) and ( int(n[-2:]) >=1) and (int(n[-2:]) <=31):
        print(f'#{i} {n[:4]}/{n[4:6]}/{n[-2:]}')
    elif (n[4:6]=='02') and (int(n[-2:])>=1) and (int(n[-2:]) <=28):
        print(f'#{i} {n[:4]}/{n[4:6]}/{n[-2:]}')
    else:
        print(f'#{i} -1')
```



## 2058 번_[자릿수 더하기](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
n=int(input())
print((n//1000)+((n%1000)//100)+(((n%1000)%100)//10)+(n%10))
```

## 2063 번_[중간값 찾기](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python

n=int(input())
v=list(map(int, input().split()))
print(sorted(v)[(n//2)])
```



## 2068 번_[최대수 구하기](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
n=int(input())
for i in list(range(1,n+1)):
    v=[]
    v=list(map(int, input().split()))
    print(f'#{i} {max(v)}')
```





## 2070 번_[큰 놈, 작은 놈, 같은 놈](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
n=int(input())
for i in list(range(1,n+1)):
    a,b=list(map(int,input().split()))
    if a<b:
        print(f'#{i} <')
    elif a==b:
        print(f'#{i} =')
    else:
        print(f'#{i} >')
```



## 2071 번_[평균값 구하기](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python
n=int(input())
for i in list(range(1,n+1)):
    v=list(map(int,input().split()))
    print(f'#{i} {int(round((sum(v)/len(v))))}')
```

## 2072 번_[홀수만 더하기](https://swexpertacademy.com/main/userpage/code/userSubmitProblem.do?userId=AXMOQ3u61tMDFAWv#none)

```python

n=int(input())
for i in list(range(1,n+1)):
    v=list(map(int, input().split()))
    v1=[]
    for j in v:
        if j %2 ==1:
            v1.append(j)
    print(f'#{i} {sum(v1)}')
```

​    