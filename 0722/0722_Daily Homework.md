# 0722_Daily Homework

## 1번

- max()
- sum()
- min()
- len()
- dir()



## 2번

```python
def get_middle_char(x):
    half=int(len(x)/2)
    if (len(x)==1) or (len(x)==2):
        return x
    elif len(x)%2 ==1:
        return x[half]
    else:
        return x[(half-1):(half+1)]
```



## 3번

`(4)` _ 인자가 두 개가 들어가면 안됨.



## 4번

#### `None`  

함수가 print, **출력**으로 끝나고 / 도출을 설정하는 **return**을 쓰지 않았기 때문



## 5번

```python
def my_avg(*args):
    result=0
    for i in args:
        result +=i
    return result/(len(args))

my_avg(77, 83, 95, 80, 70)
```





