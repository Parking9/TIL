# 1014 Workshop

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Animal API</h1>
    <button>멈뭄미 주세여</button>
    <button id='button2'>고먐미 주세여</button>
    <hr>
    <div id='animals'></div>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        const CATAPI='https://api.thecatapi.com/v1/images/search'
        const DOGAPI="https://dog.ceo/api/breeds/image/random"
        function getDog(){
            axios.get(DOGAPI)
            .then(function(res){
                const dogImg = document.createElement('img')
                // dogImg.src = res.data.message
                const dogImgSrc = res.data.message
                dogImg.setAttribute('src',dogImgSrc)
                dogImg.setAttribute('width',200)
                dogImg.setAttribute('height',300)
                dogImg.setAttribute('style','margin : 10px')
                animalsDiv.append(dogImg)
            })
            .catch(function(err){
                console.log(err)
            })
        }

        function getCat(){
            axios.get(CATAPI)
            .then(function(res){
                const catImg = document.createElement('img')
                const catImgSrc = res.data[0].url
                catImg.src=catImgSrc
                catImg.width=200
                catImg.height=300
                catImg.style.margin='10px'
                animalsDiv.append(catImg)
            })
            .catch(function(err){
                console.log(err)
            })            
        }

        const getDogButton = document.querySelector('button')
        const getCatButton = document.querySelector('#button2')
        const animalsDiv = document.querySelector('#animals')

        getDogButton.addEventListener('click', getDog)
        getCatButton.addEventListener('click', getCat)
    </script>
</body>
</html>
```

