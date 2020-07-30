# 0727_Daily Workshop

## 1번. 평균 점수 구하기

> key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의 평균점수를 반환하는 함수를 작성하시오

```python
def get_dict_avg(subject_dict):
    return sum(subject_dict.values())/len(subject_dict)

get_dict_avg({
    'python':80,
    'algorithm':90,
    'django':89,
    'web':83
    })
```



## 2번. 혈액형 분류하기

> 여러 사람의 혈액형에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 반환하는 함수를 작성하시오

```python
def count_blood(blood_list):
    ans={}
    for blood in blood_list:
        ans[blood]=ans.get(blood,0)+1
    return ans

count_blood([
    'A','B','A','O','AB','AB',
    'O','A','B','O','B','AB'])
```



