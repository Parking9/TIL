# 0721_work shops

## 1번

- `Mutable` 	   -  List,  Dictionary, set
- `Immutable`    -  String, Tuple, Range



## 2번

```python
list(range(1,51,2))
```



## 3번

```python
{'강석민':26,'강채원':25,'구영지':27,'김대중':26,'김효진':26,'박주동':27,'박철완':26,
'이동희':26,'이준희':29,'임지성':26,'허태윤':27,'홍진표':26}
```



## 4번

```python
n=5
m=9
for i in range(m):
    for j in range(n):
        print('*',end='')
    print()
```



## 5번

```python
temp=36.5
print('입실 불가') if temp >=37.5 else print('입실 가능')
```



## 6번

```python
scores=[80, 89, 99, 83]
sum_score=0
for score in scores:
    sum_score+=score
print(sum_score/len(scores))
```

```python
import numpy as np
np.mean(scores)
```

