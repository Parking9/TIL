# 1113 Workshop



## index.js

```javascript
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos : [],
  },
  mutations: {
    CREATE_TODO : function(state, todo){
      state.todos.push(todo)
    },
    DELETE_ITEM: function(state, todo){
      const idx = state.todos.indexOf(todo)
      state.todos.splice(idx,1)
    },
    SELECT_ITEM: function(state,todo){
      const idx = state.todos.indexOf(todo)
      if(state.todos[idx].checked){
        state.todos[idx].checked = false
      }else{
        state.todos[idx].checked =true
      }
    },
    DELETE_SELECTED : function(state,todos){
      state.todos = todos.filter((todo)=>{
        return !todo.checked
      })
    }
  },
  actions: {
    createTodo : function({ commit }, todo){
      commit('CREATE_TODO', todo)
    },
    deleteItem: function({commit}, todo){
      commit('DELETE_ITEM', todo)
    },
    selectItem : function({commit}, todo){
      commit('SELECT_ITEM',todo)
    },
    deleteSelected : function({commit}, todos){
      commit('DELETE_SELECTED', todos)
    }
  },
  plugins: [
    createPersistedState(),
  ],
  // watch:{
  //   todos : {
  //     deep : true,
  //     handler : function(){
        
  //     }
  //   }
  // }

})

```





## App.vue

```vue
<template>
  <div id="app">
    <h1>오늘의 할 일</h1>
    <TodoInput />
    <TodoList />
    <button @click='deleteSelected'>선택 항목 삭제</button>

  </div>
</template>

<script>
import TodoInput from '@/components/TodoInput.vue'
import TodoList from '@/components/TodoList.vue'
import {mapState} from 'vuex'


export default {
  name: 'App',
  components: {
    TodoInput,
    TodoList,
  },
  computed:{
    ...mapState([
      'todos',
    ])
  },
  methods : {
    deleteSelected : function(){
      this.$store.dispatch('deleteSelected', this.todos)
      }
    }
}



</script>

<style>

</style>

```



## TodoInput.vue

```vue
<template>
    <div>
        <input @keydown.enter='todoInput' v-model.trim='todoContent' type="text"><button @click='todoInput'>추가</button>
    </div>
</template>

<script>
// import { mapActions } from 'vuex'

export default {
    name : 'TodoInput',
    data : function(){
        return {
            todoContent : '',
        }
    },
    methods : {
        todoInput : function(){
            if (this.todoContent){
                const todo = {
                    title : this.todoContent,
                    completed : false,
                    checked : false,
                }
                this.$store.dispatch('createTodo',todo)
                this.todoContent=''
            }
        }
    }
}
</script>

<style>

</style>
```



## TodoList.vue

```vue
<template>
    <div>
        <TodoItem 
            v-for="(todo,idx) in todos"
            :key='idx'
            :todo ='todo'
        />
    </div>
</template>

<script>
import TodoItem from '@/components/TodoItem.vue'
import {mapState} from 'vuex'


export default {
    name: 'TodoList',
    components : {
        TodoItem,
    },
    computed :{
        ...mapState([
            'todos'
        ])
    }

}
</script>

<style>

</style>
```



## TodoItem

```vue
<template>
    <div>
        <input @click="todoSelect" type="checkbox"><span @>{{todo.title}}</span><button @click='deleteItem'>완료</button>
    </div>
</template>

<script>
export default {
    name : 'TodoItem',
    props : {
        todo : Object
    },
    methods :{
        deleteItem: function(){
            this.$store.dispatch('deleteItem', this.todo)
        },
        todoSelect : function(){
            this.$store.dispatch('todoSelect', this.todo)
        }
    }

}
</script>

<style>

</style>
```

