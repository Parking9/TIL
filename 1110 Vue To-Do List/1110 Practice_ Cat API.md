# 1110 Practice_ Cat API

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>고먐미</h1>
    <div id='app'>
        <button @click='addCatImg'>Get Cat</button>
        <hr>
        <img :src="imgSrc" style='width: 50vw; height: 50vh;' alt="">
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src='https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js'></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        const catAPI = 'https://api.thecatapi.com/v1/images/search'
        const vm = new Vue({
            el: '#app',
            data:{
                imgSrc :null,
                imgStyle :'',
            },
            methods:{
                addCatImg : function(){
                    axios.get(catAPI)
                    .then((res) => {
                        this.imgSrc = res.data[0].url
                    })

                    .catch(function(err){
                        console.log(err)
                    })
                }
            }
        })
    </script>
</body>
</html>
```

