# 0728_Daily Homework

## 1번.Built in 함수와 메서드

> sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오

- sorted

```python
a=[1,5,7,3,6,2]
print(sorted(a)) #[1, 2, 3, 5, 6, 7]
print(a) #[1, 5, 7, 3, 6, 2]
```

sorted() 는 list를 정렬하고 표현한다. 기존의 list를 변형시키지 않고, 정렬된 새로운 list를 반환한다.

- .sort()

```python
b=[1,5,7,3,6,2]
b.sort()
print(b.sort()) #None
print(b) #[1, 2, 3, 5, 6, 7]
```

.sort()는 기존의 list를 정렬하여 변형하는 함수이다. *sorted()와 .sort()의 차이는 기존의 list의 변형 여부이다.*



## 2번. .extend()와 append()

> .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

- extend

```python
ls1=['a','b','c']
ls1.extend('def')
print(ls1) #['a', 'b', 'c', 'd', 'e', 'f']

ls1=['1','2','3']
ls1.extend(['4','5'])
print(ls1) #['1', '2', '3', '4', '5']
```

.extend()는 괄호 안에 iterable한자료형이 들어가야한다. extend는 list 끝에 iterable의 항목을 개별적으로 삽입한다.

- append

```python
ls2=['a','b','c']
ls2.append('def')
print(ls2) #['a', 'b', 'c', 'def']

ls2=['1','2','3']
ls2.append(['4','5'])
print(ls2) #['1', '2', '3', ['4', '5']]
```

반면, .append()는 괄호안에 어떤 인자든 가능하고 리스트 끝에 받은 인자를 그대로 삽입한다.



## 3. 복사가 잘 된 건가?

> 아래의코드를 실행 하였을 때 , 변수 a 와 b 에 담긴 list 의 요소가 같은지 혹은 다른지 여부를 판단하고 그 이유를 작성하시오.

```python
a=[1,2,3,4,5]
b=a
a[2]=5
```

같다. list는 mutable 데이터로 위와 같이 b가 a와 같다고 할당 후, a를 수정하면 b도 수정된 값이 들어간다.

*이를 방지하기 위해 copy 모듈의 deepcopy() 메서드를 활용하여 b를 다른 객체로 할당하면 a를 변경해도 b는 변경되지 않는다.*