# 0723_Daily Workshop

## 1번. 숫자의 의미

```python
def get_secret_word(x):
    ans=''
    for word in x:
        ans+=chr(word)
    return ans
```



## 2번. 내 이름은 몇일까

```python
def get_secret_number(x):
    ans=0
    for i in x:
        ans+=ord(i)
    return ans
```



## 3번. 강한 이름

```python
def get_strong_word(x,y):
    ans1=0
    ans2=0
    for i in x:
        ans1+=ord(i)
    for j in y:
        ans2+=ord(j)
    if ans1>ans2:
        return x
    elif ans1==ans2:
        return('same')
    else:
        return y
```

