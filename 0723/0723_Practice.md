# 0723_Practice 

## 1번. `abs()` 직접 구현하기

> 절댓값은 숫자형 자료(int, float)가 들어오면 절댓값을 반환하고, 복소수형 자료(complex)가 들어오면 해당하는 자료의 크기를 반환합니다.
>
> 파이썬 내장 함수 `abs()`를 직접 구현한 `my_abs()`를 작성하시오.

```python
def my_abs(x):
    import math
    if type(x)==complex:
        return math.sqrt(x.real**2+x.imag**2)
    elif x==0:
        return 0
    elif x<0:
        return(-x)
    else:
        return(x)

# 아래의 코드를 실행하여 출력된 결과를 확인하시오.
print(my_abs(3+4j)) -> 5.0
print(my_abs(-0.0)) -> 0
print(my_abs(-5)) -> 5.0
print(abs(3+4j), abs(-0.0), abs(-5)) -> 5.0 0.0 5
```



## 2번. `all()` 직접 구현하기

> `all()`은 인자로 받는 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환합니다.
>
> 파이썬 내장 함수 `all()`을 직접 구현한 `my_all()`을 작성하시오.

```python
def my_all(elements):
    for element in elements:
        if not element:
            return False
    return True

# 아래의 코드를 실행하여 출력된 결과를 확인하시오.

print(my_all([])) --> True
print(my_all([1, 2, 5, '6'])) --> True
print(my_all([[], 2, 5, '6'])) --> False
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6'])) --> True True False
```



## 3번. `any()` 직접 구현하기

> `any()`는 인자로 받는 iterable(range, list)의 요소 중 하나라도 참이면 True를 반환하고, 비어있으면 False를 반환합니다.
>
> 파이썬 내장 함수 `any()`을 직접 구현한 `my_any()` 함수를 작성하시오.

```python
def my_any(elements):
    for element in elements:
        if element:
            return True
    return False

# 코드를 실행하여 결과를 확인하시오.
print(my_any([1, 2, 5, '6'])) --> True
print(my_any([[], 2, 5, '6'])) --> True
print(my_any([0])) --> False
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0])) --> True True False
```





## 4번. 불쌍한 핑핑이

> 달팽이는 낮 시간 동안에 기둥을 올라간다. 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼 미끄러진다. (낮 시간 동안 올라간 거리보다는 적게 미끄러진다.)
>
> 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 `snail()`을 작성하시오.
>
> 함수의 인자는 다음과 같다. 1. 기둥의 높이(미터) 2. 낮 시간 동안 달팽이가 올라가는 거리(미터) 3. 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)

```python
def snail(height, day, night):
    count=0
    while 1:
        if (height-day)<=0:
            return count+1
        else:
            height=height-day+night
            count+=1
            
# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(snail(100, 5, 2)) -> 33
```





## 5번. 자릿수 더하기 (SWEA #2058)

> 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.

```python
def sum_of_digit(number):
    number=str(number)
    v=[]
    for i in number:
        v.append(int(i))
    return sum(v)

# 해당 코드를 통해 올바른 결과가 나오는지 확인하시오.
print(sum_of_digit(1234)) -> 10
print(sum_of_digit(4321)) -> 10

```

