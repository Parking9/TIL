# 0728_Daily Workshop

## 1번. 무엇이 중복일까

>문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list 를 반환하는 duplicated_letters 함수를 작성하시오.

```python
def duplicated_letters(word):
    dist=[]
    for i in word:
        if word.count(i)>1:
            dist.append(i)
    return list(set(dist))

#def duplicated_letters(word):
#    return list({char for char in word if word.count(char)>=2})
```



## 2번. 소대소대

> 문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 반환하는 low_and_up 함수를 작성하시오 . 이때 , 전달 받는 문자열은 알파벳으로만 구성된다.

```python
def low_and_up(word):
    new_word=''
    for i in range(0,len(word)):
        if i in list(range(0,len(word),2)):
            new_word+=word[i].lower()
        else:
            new_word+=word[i].upper()
    return new_word

#def low_and_up(word):
#    new_word=''
#    for idx,char in enumerate(word):
#        if idx %2:
#            new_word+=char.upper()
#        else:
#            new_word+=char.lower()
#    return new_word
```



## 3번. 숫자의 의미

> 정수 0 부터 9 까지로 이루어진 list 를 전달 받아 , 연속적으로 나타나는 숫자는 하나만 남 기고 제거한 list 를 반환하는 lonely 함수를 작성하시오 . 이때 , 제거된 후 남은 수들이 담긴 list 의 요소들은 기존의 순서를 유지해야 한다.

```python
def lonely(lst):
    ans=[]
    wrd=''
    for i in lst:
        if i != wrd:
            ans.append(i)
            wrd=i
        else:
            pass
    return ans
```

