# Daily Workshop _ 박철완

## 1번

```python
number=int(input())
for i in range(1,number+1):
    print(i)
```



## 2번

```python
number=int(input())
for i in range(1,number+1):
    print(i,end=' ')
```



## 3번

```python
number=int(input())
for i in range(number,-1,-1):
    print(i)
```



## 4번

```python
number=int(input())
for i in range(number,-1,-1):
    print(i,end=' ')
```



## 5번

```python
number=int(input())
sum=0
while number>0:
    sum+=number
    number-=1
print(sum)
```