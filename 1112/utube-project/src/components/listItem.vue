<template>
  <li @click='videoDetail' id='videoItem'>
      <div>
        <img :src="imgSrc" alt="">
        <div style="display: inline-block">
            {{videoTitle | unescape}}
            {{videoChannel | unescape}}
            {{videoData}}
        </div>
      </div>
  </li>
</template>

<script>
import _ from 'lodash'

export default {
    name : 'listItem',
    props : {
        video : {
            type : Object
        }
    },
    methods : {
        videoDetail : function(){
            this.$emit('sendVideoId',this.video)
        },
    },
    computed:{
        imgSrc : function(){
            return this.video.snippet.thumbnails.default.url
        },
        videoTitle: function(){
            return this.video.snippet.title
        },
        videoChannel : function(){
            return this.video.snippet.channelTitle
        },
        videoDiscription : function(){
            return this.video.snippet.discription
        },
        videoData : function(){
            return this.video.snippet.publishedAt
        }
    },
    filters : {
        unescape : function(text){
            return _.unescape(text)
        }
    }
}
</script>

<style>
#videoItem{
    width: 30vw;
}
li{
    list-style: none;
}
li:hover{
    cursor: pointer;
    border: 0.1px lightsteelblue solid;
}
li > div{
    display:flexbox
}
img{
    width: 30%;
    height: 100%;
}
</style>

