<template>
    <div>
        <my-header></my-header>
        <div class="posts" v-for="post in postsList">
            <div class="card">
                <div class="body">
                    <h3 class="card-title">{{post.title}}</h3>
                    <p class="card-text">{{post.body}}</p>
                    <h4 class="card-text">{{post.pub_data}}</h4>
                </div>
                <div class="card-footer">
                    <button v-on:click="deletePost(post)"
                    type="submit" class="btn btn-dark">Delete</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import myHeader from './header'
export default {
    name: 'HomePage',
    data(){
        return {
            data:null
        }
    },
    components: {myHeader},
    mounted(){
        this.$store.dispatch('GET_POSTS')
    },
    computed: {
        postsList(){
            return this.$store.getters.GET_POSTS_GETTER;
        }
    }
}
</script>