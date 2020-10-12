# 1012 Workshop

## CREATE, READ

```html
function addTodo () {
  // input 요소를 선택하고, value 값을 꺼낸다.
  const input = document.querySelector('input')
  // 새로운 li 요소를 생성하고, input value를 innerText로 넣는다.
  const li = document.createElement('li')
  if (input.value!==''){
  li.innerText = input.value
  // ul 요소를 선택하고, li 요소를 자식요소로 추가한다.
  const ul = document.querySelector('ul')
  ul.appendChild(li)
  // input 요소의 value 값을 초기화한다.
  input.value=''
  }else{
    alert('***값을 넣어주세요***')
  }
}
```



## line-through Toggle, delete 까지

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TODO</title>
  <style>
    .line{
      text-decoration: line-through;
    }
  </style>
</head>
<body>
    <input type="text">     <!-- 입력을 받을 input -->
    <button>Add</button>    <!-- 클릭 시 todo item을 추가해주는 버튼 -->
    <ul>                    <!-- 순서 없는 list (Unordered List) -->
      <li>Item 1</li>       <!-- Todo Item 1 -->
      <li>Item 2</li>       <!-- Todo Item 2 -->
    </ul>

  <script>
    const input = document.querySelector('input')
    function addTodo () {
      // input 요소를 선택하고, value 값을 꺼낸다.
      // 새로운 li 요소를 생성하고, input value를 innerText로 넣는다.
      const content = input.value
      if (content){
        const li = document.createElement('li')
        li.innerText = content
        // ul 요소를 선택하고, li 요소를 자식요소로 추가한다.
        const ul = document.querySelector('ul')
        ul.appendChild(li)
        // input 요소의 value 값을 초기화한다.
        input.value=''
        li.addEventListener('click', function(event){
          event.target.classList.toggle('line')
        })

        const deletebutton = document.createElement('button')
        deletebutton.innerText='X'
        deletebutton.style.marginLeft = '10px'
        li.appendChild(deletebutton)

        deletebutton.addEventListener('click',function(){
          li.remove()
        })
      }else{
        alert('***값을 넣어주세요***')
      }
    }

    // button 요소를 선택하고, 클릭되었을 때 addTodo 함수를 실행한다.
    const button = document.querySelector('button')
    button.addEventListener('click', addTodo)
    const form = document.querySelector('form')
    input.addEventListener('keydown',function(event){
      if (event.code==='Enter'){
        addTodo()
      }
    })
  </script>
</body>
```

