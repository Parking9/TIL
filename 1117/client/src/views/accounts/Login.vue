<template>
  <div>
    <form action="" @submit.prevent='login'>
        <div>
            <label  for="userid">아이디 : </label>
            <input v-model='credentials.username' id='userid' type="text">
        </div>
        <div>
            <label for="password">비밀번호 : </label>
            <input v-model='credentials.password' id='password' type="password">
        </div>
        <button>로그인</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_MY_URL

export default {
    name : 'Login',
    data : function(){
        return {
            credentials :{
                username : '',
                password : '',
            }
        }
    },
    methods : {
      login : function(){
        axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
          .then(res=>{
            localStorage.setItem('jwt',res.data.token)
            this.$emit('loginSuccess')
            this.$router.push({name : 'TodoList'})
          })
          .catch(err => {
            console.log(err)
          })
      }
    }
}
</script>

<style>
</style>