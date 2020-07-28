# 0728_Practice

## 1번. 회문판별

> 회문 또는 팰린드롬은 거꾸로 읽어도 제대로 읽는 것과 같은 문장이나 낱말, 숫자, 문자열 등을 말한다.
>
> 입력으로 짧은 영어단어 word가 주어질 때, 해당 단어가 회문이면 True 회문이 아니면 False를 반환하는 함수를 작성하시오.
>
> 이때, 반복문(`while`)과 재귀 함수를 사용해서 각각 작성하시오.
>
> 예시)
>
> ```python
> is_pal_while('tomato') #=> False
> is_pal_while('racecar') #=> True
> is_pal_recursive('azza') #=> True
> ```



```python
# while

def is_pal_while(word):
    cnt=0
    wrd=''
    while cnt!=len(word):
        wrd=word[cnt]+wrd
        cnt+=1
    if wrd==word:
        return True
    else:
        return False

```

```python
print(is_pal_while('tomato')) #False
print(is_pal_while('racecar')) #True
print(is_pal_while('azza')) #True
```

---

```python
# recursive

def is_pal_recursive(word):
    if len(word) <=1:
        return True
    else:
        if word[0]==word[len(word)-1]:
            return is_pal_recursive(word[1:len(word)-1])
        else:
            return False
```

```python
print(is_pal_recursive('tomato')) #False
print(is_pal_recursive('racecar')) #True
print(is_pal_recursive('azza')) #True
```



## 2번. 중복되지 않은 숫자의 합

> 같은 숫자가 한개 있거나 두개가 들어있는 리스트가 주어진다. 이러한 리스트에서 숫자가 한개만 있는 요소들의 합을 구하는 함수 `sum_of_repeat_number()`를 작성하시오.
>
> 예를 들어, `[4, 5, 7, 5, 4, 8]`는 7과 8이 한번만 나오기 때문에 두개를 더한 15가 결과값으로 도출된다.
>
> 예시)
>
> ```python
> sum_of_repeat_number([4, 4, 7, 8, 10]) # => 25
> ```



```python
def sum_of_repeat_number(numbers):
    ans=[]
    for i in numbers:
        if numbers.count(i)==1:
            ans.append(i)
    return sum(ans)
```

```python
print(sum_of_repeat_number([4, 4, 7, 8, 10])) # 25
```



## 3번. 썩은 과일 찾기

> 과수원에 농부 한명이 썩은 과일이 몇개 들어있는 과일 봉지를 가지고 있다. (과일 봉지는 리스트를 의미한다.)
>
> 썩은 과일 조각들을 모두 신선한 것으로 교체하는 함수 `change_rotten_fruit()`를 작성하시오.
>
> 예를 들어,
>
> - `['apple', 'rottenBanana', 'apple']` 이라는 리스트가 주어진 경우, 대체된 리스트는 `['apple', 'banana', 'apple']` 이어야 한다.
>
> **유의**
>
> - 만약 리스트가 null/nil/None이거나 비어 있는 경우 빈 리스트를 반환한다.
> - 반환된 리스트의 요소는 모두 소문자여야 한다.
>
> 예시)
>
> ```python
> change_rotten_fruit(['apple', 'rottenBanana', 'apple']) 
> #=> ['apple', 'banana', 'apple']
> 
> change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']) 
> #=> ['apple', 'banana', 'apple', 'grape']
> ```



```python
def change_rotten_fruit(fruit_bag):
    ans=[]
    if not fruit_bag:
        return []
    else:
        for i in fruit_bag:
            if 'rotten' in i:
                ans.append(i.lstrip('rotten').lower())
            else:
                ans.append(i.lower())
    return ans
```

```python
print(change_rotten_fruit(['apple', 'rottenBanana', 'apple'] ))
# ['apple', 'banana', 'apple']
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']))
#['apple', 'banana', 'apple', 'grape']
print(change_rotten_fruit([])) #[]
```

