<template>
    <div>
        <form @submit.prevent='addTodo' action="">
            <input v-model='todo' type="text"><button>할 일 추가</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'


export default {
    name : 'CreateTodo',
    data : function(){
        return {
            todo : ''
        }
    },
    methods : {
        setToken: function(){
            const token = localStorage.getItem('jwt')
            const config ={
                headers : {
                    Authorization : `JWT ${token}`
                }
            }
            return config
        },
        addTodo : function(){
            const URL ='http://127.0.0.1:8000/todos/'
            const data = {title : this.todo}
            axios.post(URL, data, this.setToken())
              .then(() =>{
                  this.todo =''
                  this.$router.push({name :'TodoList'})
              }

              )
              .catch((err)=>{
                  console.log(err)
              })
        }
    }
}
</script>

<style>

</style>