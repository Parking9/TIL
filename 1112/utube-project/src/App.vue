<template>
  <div id="app">
    <header>
      <searchBar @sendData='dataIn' />
    </header>
    <section>
      <videoDetail :videoId='videoId' v-if="videoId" id='Video'/>
      <videoList 
      :searchedList='searchedList'
      @sendVideoId='sendVideoId'
      id='List'
      />
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import searchBar from '@/components/searchBar.vue'
import videoList from '@/components/videoList.vue'
import videoDetail from '@/components/videoDetail.vue'

const GOOGLE_API ='https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_API_KEY


export default {
  name: 'App',
  components: {
    searchBar,
    videoList,
    videoDetail,
  },
  data: function(){
    return{
      userInput:'',
      searchedList:[],
      videoId:''
    }
  },
  methods : {
    dataIn : function(data){
      this.userInput = data
      axios.get(GOOGLE_API, {
        params:{
          key : API_KEY,
          part : 'snippet',
          type : 'video',
          q : data,
        }
      })
        .then( res => {
          this.searchedList = res.data.items
        })
        .catch(err => {
          console.log(err)
        })
    },
    sendVideoId : function(data){
      this.videoId = data
    }
  }
}
</script>

<style>
/* #id{
  display:flex;
  align-items : center;
} */
#app{
  width: 100%;
}

header,
section{
  width: 80%;
  margin: 0 auto;
}

header{
  width: 100%;
  margin: 2em 0;
  text-align: center;
}

section{
  display: flex;
  align-items: center;
  margin : 0px;
}
#Video{
  width:80%
}
#List{
  width:20%

}
</style>
