<template>
    <div>
        <form action="" @submit.prevent='signup'>
            <div>
                <label  for="userid">아이디 : </label>
                <input v-model='credentials.username' id='userid' type="text">
            </div>
            <div>
                <label for="password">비밀번호 : </label>
                <input v-model='credentials.password' id='password' type="password">
            </div>
            <div>
                <label for="passwordConfirm">비밀번호 확인 : </label>
                <input v-model='credentials.passwordConfirm' id='passwordConfirm' type="password">
            </div>
            <button >회원가입</button>
        </form>
    </div>
</template>


<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_MY_URL

export default {
    name : 'Signup',
    data : function(){
        return {
            credentials :{
                username : '',
                password : '',
                passwordConfirm : '',
            }
        }
    },
    methods : {
        signup : function(){
            axios.post(`${SERVER_URL}/accounts/signup/`,this.credentials)
              .then(() => {
                  this.$router.push({name : 'Login'})
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