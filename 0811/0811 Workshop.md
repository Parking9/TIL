# 0811 Workshop

## html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="body1 bg-lgray margin4 padding4 text-center b4">
    <h1>header</h1>
  </header>
  <nav class="bg-lgray margin4 padding4 body1 b4">
    <h2>nav</h2>
  </nav>
  <section class="bg-lgray margin4 padding4 d-assign-display section-wh b4">
    <h2>section</h2>
    <article class="bg-white margin4 padding4 b4">
      <h3>article1</h3>
      <h3>article2</h3>
    </article>
  </section>
  <aside class="bg-lgray margin4 padding4 d-assign-display aside-wh v-align-top b4">
    <h2>aside</h2>
  </aside>
  <footer class="bg-lgray margin4 padding4 body1 b4">
    <h2>footer</h2>
  </footer>
</body>
</html>
```





## CSS



```css
.body1 {
  font-family: Arial;
  box-sizing: border-box;
  width: 800px;
}
/* 
.header1 {
  width: 800px;
  background-color: lightgray;
  text-align: center;
  margin: 4px;
  padding: 4px;
  border: 4px;
}
.nav1 {
  width: 800px;
  background-color: lightgray;
  text-align: left;
  margin: 4px;
  padding: 4px;  
  border: 4px;
}
.section1 {
  display: inline-block;
  width: 482px;
  height: 300px;
  background-color: lightgray;
  text-align: left;
  margin: 4px;
  padding: 4px;
  display: inline-block;
  border: 4px;
}
.aside1{
  display: inline-block;
  width: 280px;
  height: 300px;
  background-color: lightgray;
  text-align: left;
  margin: 4px;
  padding: 4px;
  vertical-align: top;
  display: inline-block;
  border: 4px;  
}
.article01 {
  background-color: white;
  margin: 4px;
  padding: 4px;
  border: 4px;
}
.footer1 {
  position: relative;
  width: 800px;
  margin: 4px;
  padding: 4px;
  background-color: lightgray;
  border: 4px;
} */
/* 모든 스타일링 요소를 클래스로 만들어 사용합니다. */

/* 1. airticle 태그는 white로 나머지 시멘틱 태그는 lightgrey로 배경색을 바꿔주세요. */
.bg-white{
  background-color: white;
}
.bg-lgray{
  background-color: lightgray;
}
/* 2. 모든 시멘틱 태그의 margin과 padding을 4px로 만들어주세요. */
.margin4 {
  margin: 4px;
}
.padding4 {
  padding: 4px;
}
/* 3. h1 태그를 중앙 정렬 시켜주세요. */
.text-center {
  text-align: center;
}

/* 4. section과 aside 태그의 display를 inline-block으로 바꿔주세요. */
.d-assign-display {
  display: inline-block;
}

/* 5. section 태그는 width 482px height 300px, aside 태그는 width 280px height 300px로 만들어주세요.*/
.section-wh {
  width: 482px;
  height: 300px;
}
.aside-wh {
  width: 280px;
  height: 300px;
}
/* 6. aside 태그에 vertical-align속성의 값을 top으로 적용해주세요.*/
.v-align-top {
  vertical-align: top;
}
/* 7. 모든 semantic 태그의 border 둘레를 4px로 만들어주세요. */
.b4 {
  border-radius: 4px;
}
```

