# 0825 Algorithm

## 4864. 문자열 비교

```python
T=int(input())
for tc in range(1, T+1):
    txt=input()
    sentc=input()
    ans=(txt in sentc)
    print(f'#{tc} {int(ans)}')
```



## 4865. 글자수

```python
T=int(input())
for tc in range(1,T+1):
    a=input()
    b=input()
    
    ans={}
    for i in a:
        if i in ans.keys():
            pass
        else:
            for j in b:
                if i==j:
                    ans[i]=ans.get(i,0)+1
    max_ans=0
    for k in ans.values():
        if k > max_ans:
            max_ans=k
    print(f'#{tc} {max_ans}')
```



## 4861. 회문

```python
def palindrome(x):
    if x==x[::-1]:
        return x
    else:
        None

T=int(input())
for tc in range(1,T+1):
    dim, len1 = map(int,input().split())
    arr=[input() for _ in range(dim)]
    ans=[]
    for i in arr:
        for i2 in range(0,dim-len1+1):
            if palindrome(i[i2:i2+len1]) != None:
                ans.append(palindrome(i[i2:i2+len1]))
    for j in range(dim):
        for j2 in range(0, dim-len1+1):
            sent=''
            for j3 in range(j2,j2+len1):
                sent+=arr[j3][j]
            if palindrome(sent) != None:
                ans.append(palindrome(sent))
                break
    print(f'#{tc} {ans[0]}')
```



## 1216. 회문2

```python
# 회문 2
def palindrome(x):
    if x==x[::-1]:
        return x

def palindrome2(arr,N,k):
    for i in range(N):
        for i2 in range(0, N-k+1):
            if palindrome(arr[i][i2:i2+k]) !=None:
                return k
            sent=''
            for j in arr[i2:i2+k]:
                sent+=j[i]
            if palindrome(sent) !=None:
                return k

for tc in range(1,11):
    n=int(input())
    arr=[input() for _ in range(100)]
    ans=0
    if palindrome2(arr, 100, 50) ==None:        
        for numb in range(50,2,-1):
            if palindrome2(arr,100,numb) != None:
                ans= palindrome2(arr,100,numb)
                break
            else:
                pass
        print(f'#{tc} {ans}')
    else:
        for numb in range(100,49,-1):
            if palindrome2(arr,100,numb) != None:
                ans= palindrome2(arr,100,numb)
                break
            else:
                pass
        print(f'#{tc} {ans}')        

```

