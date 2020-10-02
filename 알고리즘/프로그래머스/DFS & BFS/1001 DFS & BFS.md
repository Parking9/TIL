# DFS & BFS

## 1번. 타겟넘버

```python
# 프로그래머스 DFS/BFS 1번
cnt=0
def dfs(x,n,numbers,N,target):
    global cnt
    if n==N:
        if eval(x)==target:
            cnt+=1
        return
    y=numbers[n]
    dfs(x+'+'+str(y),n+1,numbers,N,target)
    dfs(x+'-'+str(y),n+1,numbers,N,target)

def solution(numbers, target):
    N=len(numbers)
    x=''
    n=0
    dfs(x,n,numbers,N,target)
    return cnt
```

++ 다른 사람의 풀이로 생각 했던 부분집합, 비트 연산자 활용 풀이가 있었음.

```python
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, list(product(*l)))
    return s.count(target)

```









## 2번. 네트워크

```python
## DFS BFS 2번.
def solution(n, computers):
    ans=0
    v=[0]*n
    Q=[]
    for i in range(n):
        if v[i]==0:
            if computers[i].count(1)==1:
                ans+=1
                v[i]=1
            elif computers[i].count(1)>1:
                v[i]=1
                Q.append(i)
                while Q !=[]:
                    w=Q.pop(0)
                    A=[x for x in range(n) if computers[w][x]==1 and v[x]==0]
                    Q+=A
                    for j in A:
                        v[j]=1
                ans+=1
    return ans

```




