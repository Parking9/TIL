<template>
  <div>
    <ul>
      <li v-for='(todo,idx) in todos' :key='idx'><span :class='{done : todo.completed}' @click='updateTodo(todo)'>{{todo.title}}</span>
        <button @click="deleteTodo(todo)">삭제</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
const MY_URL = process.env.VUE_APP_MY_URL

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: [],
    }
  },
  methods: {
    setToken: function(){
        const token = localStorage.getItem('jwt')
        const config ={
            headers : {
                Authorization : `JWT ${token}`
            }
        }
        return config
    },    
    getTodos: function () {
      axios.get(`${MY_URL}/todos/`,this.setToken())
        .then(res => {
          console.log(res)
          this.todos = res.data
        })
        .catch(err => console.log(err))
    },
    deleteTodo : function(todo){
      axios.delete(`${MY_URL}/todos/${todo.id}/`,this.setToken())
        .then(() => {
          const idx = this.todos.findIndex(item => {
            return item.id === todo.id
          })
          this.todos.splice(idx,1)
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateTodo : function(todo){
      const data = {
        ...todo,
        completed : !todo.completed
      }
      axios.put(`${MY_URL}/todos/${todo.id}/`, data,this.setToken())
        .then(() =>{
          todo.completed = !todo.completed
        })
        .catch(err=>{
          console.log(err)
        })
    }
  },
  created: function () {
    this.getTodos()
  },
  watch : {
    todos : function(){
      return this.todos
    }
  }
}
</script>

<style>
.done{
  text-decoration: line-through;
  color: gray;
}
li:hover{
  cursor: pointer;
}
</style>