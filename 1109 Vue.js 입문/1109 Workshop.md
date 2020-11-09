# 1109 Workshop

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <div id='app'>
        <h1>점심메뉴</h1>
        <button @click='getMenu'>Pick One</button>
        <p>{{todayLunch}}</p>
        <hr>
        <h1>로또</h1>
        <button @click='getNumbers'>Get Lucky Numbers</button>
        <p>{{ num }}</p>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src='https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js'></script>
    <script>
        const app = new Vue({
            el: '#app',
            data: {
                menuList: ['국밥', '짬뽕', '짜장면', '해장국', '치킨', '보쌈'],
                todayLunch: '',
                num: ''

            },
            methods: {
                getMenu: function () {
                    const idx = _.sample(this.menuList)
                    this.todayLunch = idx

                },
                getNumbers: function () {
                    const numbers = _.range(1, 46)
                    randomNumber = _.sampleSize(numbers, 6)
                    this.num = _.sortBy(randomNumber)
                }
            }
        })
    </script>
</body>

</html>
```

