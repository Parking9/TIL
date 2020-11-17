<template>
  <div id="app">
    <div id="nav">
      <template v-if="login">
        <router-link :to="{ name: 'TodoList' }">Todo List</router-link> |
        <router-link :to="{ name: 'CreateTodo' }">Create Todo</router-link> |
        <router-link @click.native='logout' to="#">Logout</router-link> |
        
      </template>
      <template v-else >
        <router-link :to="{ name: 'Signup' }">Sign up</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </template>
    </div>
    <router-view @loginSuccess='login = true'/>
  </div>
</template>

<script>
export default {
  name: 'APP',
  data : function(){
    return {
      login : false
    }
  },
  created : function(){
    const key = localStorage.getItem('jwt')
    if(key){
      this.login = true
    }
    return this.login
  },
  methods :
  {
    logout : function(){
     localStorage.removeItem('jwt')
     this.login = false
     this.$router.push({name : 'Login'})
   } 
  },
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
