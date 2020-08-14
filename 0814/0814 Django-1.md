# 8월 14일 수요일

Model - 데이터 관리

Template - 인터페이스 (화면)

View - 중간 관리 (상호 동작)



코드 작성 순서 == 데이터의 흐름과 같음

1. urls.py
2. views.py
3. templates





* Django 개발 환경 세팅
  * Python 3.7.7 확인
  * Django Package 설치
  * Django Extension 설치 및 Emmet 설정

---

* Django 프로젝트 생성

  ```bash
  # 새로운 폴더를 만든 뒤, 그 안에 프로젝트 폴더와 manage.py를 생성한다.
  $ django-admin startproject 프로젝트이름
  
  # 현재 경로에서 프로젝트 폴더와 manage.py를 생성한다.
  $ django-admin startproject 프로젝트이름 .
  ```

  ```
  0814/
     my_project/            - 최상위 디렉토리명은 자유롭게 바꿀 수 있다.
         first_project/     - 실제 장고 프로젝트 폴더명은 바꾸면 안된다.
         manage.py
  ```

  ```
  movie_project/
     movie_project/
     manage.py
  ```



* **서버 실행 확인**

  * 명령어를 실행하는 경로가 `manage.py`가 있는 경로인지 확인한다!

  ```bash
  $ python manage.py runserver
  ```



* **Django 애플리케이션 생성**

  * 명령어를 실행하는 경로가 `manage.py`가 있는 경로인지 확인한다!

  ```bash
  $ python manage.py startapp 애플리케이션이름
  ```



* **기본 환경설정 (settings.py )**

  ```python
  # settings.py
  
  INSTALLED_APPS = [
      'articles',
      ...
      ...
  ]
  
  LANGUAGE_CODE = 'ko-kr'
  
  TIME_ZONE = 'Asia/Seoul'
  ```

  

* **URL 연결 (프로젝트 폴더/urls.py)**

  ```python
  # urls.py
  
  urlpatterns = [
      path('admin/', admin.site.urls),
  
      # 사용자가 hello/ 라는 주소로 요청을 하면,
      # hello 함수(기능)를 실행해라!
      path('hello/', views.hello),
  ]
  ```



* **기능 정의 (애플리케이션 폴더/views.py)**

  ```python
  # views.py 
  
  from django.shortcuts import render
  
  # Create your views here.
  def hello(request):
      name = '채원'
      context = {
          # 왼쪽 : 템플릿에서 사용할 이름
          # 오른쪽 : 현재 함수 내에서 사용한 이름 (넘겨줄 변수, 데이터)
          'chaewon': name,
      }
      return render(request, 'hello.html', context)
  ```

  

* **사용자에게 보여줄 템플릿 정의 (애플리케이션 폴더/templates/)**

  ```html
  <!-- hello.html -->
  
  <h1>채원 안녕!</h1>
  <h2>{{ chaewon }}, 안녕하세요!</h2>
  ```

  

---



* 장고로 만들어진 웹 애플리케이션이라고 생각해보자!
  1. 사용자가 요청한 URL을 분석하여 적절한 기능으로 연결시켜준다 -> `urls.py`
  2. 기능을 실행하여 **데이터를 가공한 뒤** 사용자에게 화면을 렌더링해준다 -> `views.py`
  3. 사용자에게 보여줄 화면은 `templates` 폴더 안에 위치시킨다



은행 : Django로 만들어진 서비스

고객 : 사용자



키오스크에서 '대출'버튼 누르기 == 사용자가 브라우저 URL 입력하고 엔터 누르기

직원 안내에 따라 대출 창구로 이동하기 == urls.py - path('대출/', views.대출창구)

5만원 출금 신청하고 5만원 받기 == views.py - def 대출(request): ~

5만원을 예쁜 봉투에 담아서 건네주기 == 템플릿 HTML 코드에 예쁘게 담아서 사용자에게 돌려주기



#### DTL (Django Template Language)

- 장고 템플릿 시스템에서 사용하는 built-in template system이다.
- 조건, 반복, 치환, 필터, 변수 등의 기능을 제공
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- 파이썬처럼 if, for를 사용할 수 있지만 단순히 python code로 실행되는 것이 아니다.



syntax

- variable : `{{ }}`

- filter : `{{ variable|filter}}`

- tags : `{% tag %}` 



## 템플릿 시스템 설계 철학

- 장고는 템플릿 시스템이 표현을 제어하는 도구이자, 표현에 관련된 로직일 뿐이라고 생각한다.
- 템플릿 시스템에서는 이러한 기본 목표를 넘어서는 기능을 지원해서는 안된다.







