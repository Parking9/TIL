# 0814 Homework shop

## 1번. settings

`TIME_ZONE`을 `Asia/Seoul`로 바꾼다.

```py
TIME_ZONE = 'Asia/Seoul'
```



## 2번. urls

```py
'ssafy/', views.ssafy
```



## 3번. Django Tempate Language

#### 1) menus 리스트를 반복문으로 출력하시오

​	`menu`



#### 2) posts 리스트를 반복문을 활용하여 0번 글 부터 출력하시오

​	`forloop.counter`



#### 3) users 리스트가 비어있다면 현재 가입한 유저가 없습니다. 텍스트를 출력하시오

​	`empty`



#### 4) 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오.

​	`if`

​	`else`



#### 5) 출력된 결과가 주석과 같아지도록 하시오

​	`length`

​	`title`



#### 6) 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 하시오.

​	`Y년 M월 d일 (D) A h:s`

## 4번. Form tag

#### 1)

​	입력한 데이터를 어느 링크로 넘길것인가

#### 2)

​	GET

#### 3)

​	http://127.0.0.1:8000/안녕하세요&content=반갑습니다&my-site=파이팅

