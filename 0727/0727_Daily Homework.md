# 0727_Daily Homework

## 1번. 모음은 몇 개나 있을까?

> 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 함수를 작성하시오 (단, count()를 활용)

```python
def count_vowels(string):
    return (string.count('a')+string.count('e')+string.count('i')+
            string.count('o')+string.count('u'))
count_vowels('apple')
count_vowels('banana')
```





## 2번. 문자열 조작

 `4번` --> 특정 문자를 지정하지 않으면, 공백을 제거한다.



## 3번. 정사각형 만들기

> 각각 너비와 높이의 값으로 이루어진 2개의 list를 전달 받아, 각각의 값들을 조정하여 만들 수 있는 정사각형만의 넓이를 담은 list를 반환하는 함수를 작성하시오

```python
def only_square_area(x,y):
    ans=[]
    for i in list(set(x)&set(y)):
        ans.append(i**2)
    return ans

only_square_area([32,55,63],[13,32,40,55])

```

