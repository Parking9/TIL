# 0721_homework

## 1번

```python
N=int(input())

for i in range(1,N+1):
    if N%i==0:
        print(i,end=' ')
```



## 2번

```python
numbers = [
    85,72,38,80,69,65,68,96,22,49,67,
    51,61,63,87,66,25,80,83,71,60,64,
    52,90,60,49,31,23,99,94,11,25,24
]

sorted(numbers)[round(len(numbers)/2)]
```



## 3번

```python
number=int(input())

for i in range(1,number+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()
```



## 4번

```python
for i in range(2,10):
    print(f'-------  [{i} 단]  -------')
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}')
    print()
```

