# 0722_ Daily Workshop

## 1번

```python
def list_sum(x):
    result=0
    for i in x:
        result +=i
    return result

```



## 2번

```python
def dict_list_sum(x):
    result=0
    for i in x:
        result +=i['age']
    return result
```



## 3번

```python
def all_list_sum(x):
    result=0
    for i in x:
        for j in i:
            result +=j
    return result
```

