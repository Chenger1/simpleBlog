<template>
    <div>
        <my-header></my-header>
        <h2>{{user_info.username}} - {{user_info.email}}</h2>
        <div class="container">
            <div class="row">
                <div class="col">
                    <h4>Posts</h4>
                    <div class="post" v-for="post in user_info.posts">
                        <div class="card">
                            <div class="body">
                                <h3 class="card-title">{{post.title}}</h3>
                                <p class="card-text">{{post.body}}</p>
                                <h4 class="card-text">{{post.pub_data}}</h4>
                            </div>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item"
                                v-for="comment in user_info.comments" v-if="comment.post_id==post.id || get_user_roles.indexOf('Admin')!=-1">
                                    <span>
                                        {{comment.body}} 
                                        <h6>
                                            User - {{comment.author}}.
                                            Data- {{comment.pub_data}}.
                                        </h6>
                                    </span>
                                </li>
                            </ul>
                            <div class="card-footer" v-if="get_username==user_info.username || get_user_roles.indexOf('Admin')!=-1">
                                <button v-on:click="deletePost(post)"
                                type="submit" class="btn btn-dark">Delete Post</button>
                                <router-link tag="button"
                                class="btn btn-dark"
                                :to="{name: 'editPost', params:{id:post.id}}">Edit Post</router-link>
                            </div>
                         </div>
                    </div>
                </div>
                <div class="col">
                    <h4>Comments</h4>
                    <div class="comment" v-for="comment in user_info.comments">
                        <div class="card">
                            <p>{{comment.body}}</p>
                            <h5>{{comment.pub_data}}</h5>
                            <div class="card-footer"  v-if="get_username==user_info.username || 'Admin ' in get_user_roles">
                                <button v-on:click="deleteComment(comment)"
                                type="submit" class="btn btn-dark">Delete Comment</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>    
</template>
<script>
import myHeader from '../header'
export default {
    name: 'userProfile',
    data() {
        return {
            user: {
                username: this.$route.params.username
            }
        }
    },
    components: {myHeader},
    created(){
        this.$store.dispatch('GET_USER_DATA', this.user.username)
    },
    methods:{
        deletePost(post){
        if(this.get_username==this.user_info.username || this.get_user_roles.indexOf('Admin')!=-1){
            let payload = {
                'post':post,
                'username': this.get_username
            }
            this.$store.dispatch('DELETE_POST', payload)
            .then(response=>{
                this.$store.dispatch('GET_USER_DATA', this.user_info.username)
                })
            };
        },
        deleteComment(comment){
            if(this.get_username==this.user_info.username || this.get_user_roles.indexOf('Admin')!=-1){
                let payload = {
                    'comment': comment,
                    'username': this.get_username
                }
                this.$store.dispatch('DELETE_COMMENT', payload)
                .then(response=>{
                    this.$store.dispatch('GET_USER_DATA', this.user_info.username)
                })
            }
        }
    },
    computed: {
        user_info(){
            return this.$store.getters.GET_USER_INFO;
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
