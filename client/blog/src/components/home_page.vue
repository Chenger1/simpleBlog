<template>
    <div>
        <my-header></my-header>
        <div class="posts" v-for="post in postsList">
            <div class="card">
                <div class="body">
                    <h3 class="card-title">{{post.title}}</h3>
                    <p class="card-text">{{post.body}}</p>
                    <h4 class="card-text">{{post.pub_data}}</h4>
                    <router-link :to="{name:'userProfile', params:{username:post.author}}">{{post.author}}</router-link>
                </div>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item"
                    v-for="comment in post.comments">
                        <span>
                            {{comment.body}} 
                            <h6>
                                User - <router-link :to="{name:'userProfile', params:{username:comment.author}}">{{comment.author}}</router-link>.
                                Data- {{comment.pub_data}}.
                            </h6>
                            <button v-on:click="deleteComment(comment)" type="submit" v-if="get_username==comment.author || get_user_roles.indexOf('Admin')!=-1"
                            class="btn btn-light">Delete Comment</button>
                            <router-link v-if="get_username==comment.author || get_user_roles.indexOf('Admin')!=-1" tag="button"
                            class="btn btn-dark"
                            :to="{name: 'editComment', params:{post_id:post.id, comment_id:comment.id, body:comment.body}}">Edit comment</router-link>
                        </span>
                    </li>
                </ul>
                <div class="card-footer" v-if="get_username==post.author || get_user_roles.indexOf('Admin')!=-1">
                    <button v-on:click="deletePost(post)"
                    type="submit" class="btn btn-dark">Delete Post</button>
                    <router-link tag="button" v-if="get_username==post.author || get_user_roles.indexOf('Admin')!=-1"
                    class="btn btn-dark"
                    :to="{name: 'editPost', params:{id:post.id}}">Edit Post</router-link>
                    <router-link tag="button"
                    class="btn btn-dark"
                    :to="{name: 'createComment', params:{id:post.id}}">Create comment</router-link>
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
            data: null
        }
    },
    components: {myHeader},
    mounted(){
        this.$store.dispatch('GET_POSTS')
    },
    methods:{
        deletePost(post){
        if(this.get_username==post.author || this.get_user_roles.indexOf('Admin')!=-1){
            let payload = {
                'post':post,
                'username': this.get_username
            }
            this.$store.dispatch('DELETE_POST', payload)
            .then(response=>{
                this.$store.dispatch('GET_POSTS')
                })
            };
        },
        deleteComment(comment){
            if(this.get_username==comment.author || this.get_user_roles.indexOf('Admin')!=-1){
                let payload = {
                    'comment': comment,
                    'username': this.get_username
                }
                this.$store.dispatch('DELETE_COMMENT', payload)
                .then(response=>{
                    this.$store.dispatch('GET_POSTS')
                })
            }
        }
    },
    computed: {
        postsList(){
            return this.$store.getters.GET_POSTS_GETTER;
        },
        get_username(){
            return this.$store.getters.GET_USERNAME;
        },
        get_user_roles(){
            return this.$store.getters.GET_USER_ROLE;
        }
    }
}
</script>