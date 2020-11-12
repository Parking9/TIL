<template>
    <div id='searchBar'>
        <input placeholder="검색" v-model='userInput' type="text" @keydown.enter='sendData'>
    </div>
</template>

<script>
export default {
    name : 'searchBar',
    data : function(){
        return {
            userInput :''
        }
    },
    methods:{
        sendData : function(){
            this.$emit('sendData',this.userInput)
        }
    }
}
</script>

<style>
#searchBar>input{
    width: 30vw;
    height: 2.5vh;
    font-size: 1rem;
}
</style>