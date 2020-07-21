# Daily Homework_ 박철완

## 1번

- !, @, #, $, % 등 특수기호

- 숫자로 시작하는 식별자

- 키워드



## 2번

```python
import math, sys

num1=0.1*3
num2=0.3

math.fabs(num1 - num2) <= sys.float_info.epsilon #True이면 같다
```



## 3번

- \n

- \t

- \\\



## 4번

```python
name='철수'
print(f'안녕, {name}야')
```



## 5번

- int('3.5')

int(float('3.5'))가 맞다. --> 3  또는 float('3.5') --> 3.5



## 6번

```python
print(('*'*n+'\n')*m)
```



## 7번

```python
print('\"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
```



## 8번

```python
import math
answer1, answer2 = (-b + math.sqrt(b**2 -4*a*c))/2*a, (-b - math.sqrt(b**2 -4*a*c))/2*a
print(answer1, answer2)
```

