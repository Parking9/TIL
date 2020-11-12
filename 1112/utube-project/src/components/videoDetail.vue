<template>
<div class='video-Detail'>
  <iframe :src="videoSrc" frameborder="0" width=90% height='470' allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <h3>{{videoTitle | unescape}}</h3>
  <div>{{videoDiscription | unescape}}</div>
  {{videoChannel}}
  {{videoData}}
</div>
</template>

<script>
import _ from 'lodash'

export default {
    name : 'videoDetail',
    props : {
        videoId : {
            type : [Object || String]
        }
    },
    computed : {
        videoSrc : function(){
            console.log(this.videoId)
            return `https://www.youtube.com/embed/${this.videoId.id.videoId}`
        },
        videoTitle: function(){
            return this.videoId.snippet.title
        },
        videoChannel : function(){
            return this.videoId.snippet.channelTitle
        },
        videoDiscription : function(){
            return this.videoId.snippet.description
        },
        videoData : function(){
            return this.videoId.snippet.publishedAt
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
.video-Detail{
    width:70%;
}


</style>