# 1110 Todo List

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .done{
            text-decoration: line-through;
            color : grey;
        }
    </style>
</head>
<body>
    <h1>To-Do List</h1>
    <div id='app'>
        <div>
            <select v-model='category'>
                <option value="all">전체</option>
                <option value="ing">미완료</option>
                <option value="done">완료</option>
            </select>
            <form action='' style='display: inline-block;' @submit.prevent='addTodo'>
                <input v-model='newTodo' type="text"><button type="submit">+</button>
            </form>
        </div>
        <ul v-for='todo in todoListByStatus' :key='todo.id'>
            <li style="list-style: none;"><input v-model='todo.completed' type="checkbox"><span :class='{done : todo.completed}'>{{todo.content}}</span><button @click='deleteOne'>삭제</button></li>
        </ul>
        <button @click='deleteDone'>완료된 할 일 지우기</button><button @click='deleteAll'>전체 삭제</button>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src='https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js'></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        const STORAGE_KEY='Todo APP By Vue'
        const todoStorage ={
            save: function(todoList){
                localStorage.setItem(STORAGE_KEY, JSON.stringify(todoList))
            },
            fetch : function(){
                return JSON.parse(localStorage.getItem(STORAGE_KEY)) || []
            },

        }


        const vm = new Vue({
            el : "#app",
            data :{
                todoList : todoStorage.fetch(),
                newTodo : '',
                category: 'all',
                oneID : '',
            },
            methods :{
                addTodo : function(){
                    const todo ={
                        id : new Date().getTime(),
                        content : this.newTodo,
                        completed : false
                    }
                    if((todo.content === '') | (todo.content===' '.repeat(todo.content.length))){
                        alert('값을 입력하세요')
                    }else{
                    this.todoList.push(todo)
                    this.newTodo=''
                    }
                },
                deleteDone : function(){
                    this.todoList = this.todoList.filter(function(todo){
                        return !todo.completed
                    })
                },
                deleteAll : function(){
                    this.todoList = []
                },
                deleteOne : function(){
                    this.todoList = this.todoList.filter(function(list){
                        return list.id !==todo.id
                    })
                }
            },
            computed :{
                todoListByStatus: function(){
                    return this.todoList.filter(todo => {
                        if(this.category==='ing'){
                            return !todo.completed
                        }else if(this.category ==='done'){
                            return todo.completed
                        }else{
                            return todo
                        }
                    })
                }
            },
            watch:{
                todoList: {
                    deep : true, //중첩된 데이터까지 감시하도록 설정
                    handler : function(){ //데이터가 변경되었을때 수행하는 로직
                        todoStorage.save(this.todoList)
                    }
                }
            }
        })
    </script>
</body>
</html>
```

