<template>
    <ul class='video-list'>
        <listItem
        v-for="(video,idx) in searchedList"
        :key ='idx'
        :video='video'
        @sendVideoId ='sendVideoId'
        />
    </ul>
</template>

<script>
import listItem from '@/components/listItem.vue'

export default {
    name : 'videoList',
    components:{
        listItem
    },
    data :function(){
        return {
            videoId : {},
        }
    },
    props : {
        searchedList : {
            type : Array,
        }
    },
    methods : {
        sendVideoId : function(data){
            this.videoId = data
            this.$emit('sendVideoId', this.videoId)
        }
    }

}
</script>

<style>
ul{
    margin: 0;
    padding: 0;
    width: 30%;
}
</style>