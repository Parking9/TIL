# 0811 Homework

## 1번. Semantic Tag

```
header, h1, section, footer
```



## 2번. Input Tag

```html
<!DOCTYPE html>
<html lang="ko">
    <form action="GET">
        <div>
            <label for="이름">USERNAME : </label>
            <input type="text" id="이름" placeholder="아이디를 입력 해 주세요." autofocus>
        </div>
        <div>
            <label for="암호">PWD : </label>
            <input type="password" id="암호" autofocus>
        </div>
    	<input type="submit" value="로그인">
    </form>
</html>

```



## 3번. 크기 단위

- rem



## 4번. 선택자

- 자손 선택자는 특정 요소 div의 하위 후손들을 모두 선택하는 선택자이다. 위 예제는 div에 있는 p 요소와 그 후손 들까지 crimsom색으로 표시된다.
- 반면, 자식 선택자는 특정요소 div의 직계 후손들만 선택하는 선택자이다. 위 예제에서는 div의 바로 한 단계 아래인 p요소만 crimsom색으로 표시된다.