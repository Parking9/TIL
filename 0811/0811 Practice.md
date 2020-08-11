# 0811 Practice

## 1번. Box Model

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BOX Model Practice</title>
  <link rel="stylesheet" href="box_model.css">
</head>
<body>
  <div class="big-box">
    <div class="small-box" id="red"></div>
    <div class="small-box" id="gold"></div>
    <div class="small-box" id="green"></div>
    <div class="small-box" id="blue"></div>
    <div class="small-box" id="pink"></div>
  </div>
</body>
</html>

```

```css
.big-box {
  position: relative;
  margin: 100px auto 500px;
  border: 5px solid black;
  width: 500px;
  height: 500px;
}

.small-box {
  width: 100px;
  height: 100px;
}

#red {
  position : absolute;
  background-color: red;
  bottom: 0;
  right: 0;
  /* 큰 사각형 내부의 우측 하단 모서리에 빨간 사각형 위치시키기 */
  
}

#gold {
  position : fixed;
  background-color: gold;
  right: 50px;
  bottom: 50px;
  /* 브라우저의 하단에서 50px, 우측에서 50px 위치에 고정하기 */
  
}

#green {
  position : absolute;
  background-color: green;
  top: 200px;
  left: 200px;
  /* 큰 사각형의 가운데 위치시키기 */

}

#blue {
  background-color: blue;
  position: absolute;
  top: 100px;
  left: 100px;
  /* 큰 사각형 좌측 상단 모서리에서 100px, 100px 띄우기 */

}

#pink {
  background-color: pink;
  position: absolute;
  margin: 0px auto auto 0px;
  /* 큰 사각형 내부의 좌측 상단 모서리로 옮기기*/
  
}

```

![result](practice/images/result.JPG)



## 2번. CSS Styling



```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="card.css">
  <title>Layout</title>
</head>
<body>
  <div class="container">
    <div class="card">
      <div class="card-nav">
        <h2>오늘의 명소</h2>
      </div>
      <div class="card-header">
        <img src="images/image.png" alt="card image" class="card-img">
        <div class="card-img-description">
          <h4>제주도</h4>
          <h4>성산 일출봉</h4>
        </div>
      </div>
      <div class="card-body">
        <div class="card-body-title">
          <h4>제주도 서귀포시 성산읍</h4>
          <p>2020.03.23</p>
        </div>
        <hr />
        <div class="card-body-content">
          <p>
            성산일출봉은 제주도의 다른 오름들과는 달리 마그마가 물속에서 분출하면서 만들어진 수성화산체다.
            화산활동시 분출된 뜨거운 마그마가 차가운 바닷물과 만나면서 화산재가 습기를 많이 머금어 끈끈한 성질을 띄게 되었고,
            이것이 층을 이루면서 쌓인 것이 성산일출봉이다.
          </p>
        </div>
      </div>
      <div class="card-footer">
        <div>&copy; SSAFY</div>
      </div>
    </div>
  </div>
</body>
</html>
```

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

p {
  font-family: Arial;
}

h4 {
  font-size: 20px;
  font-weight: bold;
}


.card {
  width: 700px;
  border: 3px dashed black;
}

.card-nav{
  text-align: center;
  background-color: mediumseagreen;
}

.card-header {
  padding: 18px;
}

.card-img {
  width: 100%;
  height: 330px;
  display: block;
}
.card-img-description {
  background-color: yellowgreen;
  text-align: center;
  color: white;
  height: 70px;
  line-height: 30px;
}

.card-body {
  padding: 18px;
}

.card-body-title {
  position: relative;
  background-color: ivory;
}

.card-body-title > h4 {
  display: inline-block;
}

.card-body-title > p {
  position: absolute;
  display: inline-block;
  right: 0;
  bottom: 0;
}

.card-body-content {
  background-color: antiquewhite;
  margin-top: 8px;
  padding: 10px;
}

.card-footer {
  background-color: forestgreen;
  color: white;
  text-align: right;
  padding: 10px 10px 10px 0;
}


```

![ex2](practice/images/ex2.JPG)