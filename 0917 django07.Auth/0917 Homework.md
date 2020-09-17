# 0917 Homework

## 1번. User Model BoolenField

- is_staff

- is_active

- is_superuser



## 2번. username max length

150



## 3번. login validation

is_authenticated

is_anonymous



## 4번. Login

(a) - AuthenticationForm

(b) - login

(c) - form.get_user()



## 5번. who are you?

AnonymousUser



## 6번. 암호화 알고리즘

알고리즘 - PBKDF2

해쉬함수 - SHA256



## 7번. Logout

logout이라는 함수 이름이 중복됐음.

`from django.contrib.auth import logout as auth_logout`을 추가하고

2번째 로그아웃 과정을 `auth_logout(request)`로 바꾼다.