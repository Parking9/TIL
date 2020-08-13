# 0813 Homework

## 1번. CSS flex-direction

- `row`                        : 주축은 인라인 방향으로 행을 따른다.
- `row-reverse`       :  주축이 인라인 방향으로 행을 따르고, 역순으로 정렬된다.
- `column`                  : 주축이 페이지 상단에서 하단으로 블록 방향을 따른다.
- `column-reverse` :  주축이 페이지 하단에서 상단으로 블록 방향을 따른다.



## 2번. Bootstrap flex-direction

- `flex-row`
- `flex-row-reverse`
- `flex-column`
- `flex-column-reverse`



## 3번. align-items

- `stretch`- 기본값. 컨테이너에 맞게 항목이 늘어난다.

- `flex-start` - 항목이 컨테이너 상단에 배치된다.

- `flex-end` - 항목은 컨테이너 하단에 위치한다.

- `center` - 항목이 컨테이너의 가운데에 위치한다.

- `baseline` - 항목이 컨테이너의 기준선에 배치된다.



## 4번. flex-flow

`(1) flex-dirction, flex-wrap`



## 5번. Bootstrap Grid System

`(a)` - container

`(b)` - row



## 6번. Breakpoint prefix

- `(c)` : container의 크기 별 입력을 할 수 있다.
  - None (auto) : 딱히 사이즈별 설정을 안한것으로, 모든 크기의 container
  - sm : 540px 이상, 768px 미만의 width를 갖는 container에 대한 설정
  - md : 768px 이상, 992px 미만의 width를 갖는 container에 대한 설정
  - lg : 992px 이상, 1200px 미만의 width를 갖는 container에 대한 설정
  - xl : 1200px 이상의 width를 갖는 container에 대한 설정

- `(d)` : 해당 container에서 차지할 부분을 나타내는 값
  - None, 1, 2 , ...., 12
  - 각각 1 ~ 12 (max) 의 크기를 차지하고, None은 자동으로 채워준다.