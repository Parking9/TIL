# 0921 Homework

## 1번. Lookup

- __gt   : Greater than
- __gte :  Greater than or equal to
- __lt    : Less than
- __lte  : Less than or eqal to



- __startswith   : 특정 문자열로 시작하는지
- __endswith  : 특정 문자열로 끝나는지



- __contains : 문자열 포함 여부
-  `__in` , ` __exat` 등...



## 2번.  1:N 관계 설정

`CASCADE`  : ForeignKeyField가 바라보는 값이 삭제될 때 ForeignKeyField를 포함하는 모델 인스턴스(row)도 삭제된다

`PROTECT`  : ForeignKeyField가 바라보는 값이 삭제될 때 삭제가 되지않도록 ProtectedError를 발생시킨다.

`SET_NULL` : ForeignKeyField가 바라보는 값이 삭제될 때 ForeignKeyField값을 null로 바꾼다. (null=True일 때만 가능)



## 3번. comment create

commit=False



## 4번. 

comments