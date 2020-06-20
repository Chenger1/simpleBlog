<template>
    <div>
        <my-header></my-header>
        <h2>{{user.username}}</h2>
        <div class="container">
            <div class="row">
                <div class="col">
                    <h4>Posts</h4>
                    <div class="post" v-for="post in user.posts">
                        <div class="card">
                            <div class="body">
                                <h3 class="card-title">{{post.title}}</h3>
                                <p class="card-text">{{post.body}}</p>
                                <h4 class="card-text">{{post.pub_data}}</h4>
                            </div>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item"
                                v-for="comment in post.comments">
                                    <span>
                                        {{comment.body}} 
                                        <h6>
                                            User - {{comment.author}}.
                                            Data- {{comment.pub_data}}.
                                        </h6>
                                    </span>
                                </li>
                            </ul>
                            <div class="card-footer">
                                <button v-on:click="deletePost(post)"
                                type="submit" class="btn btn-dark">Delete Post</button>
                            </div>
                         </div>
                    </div>
                </div>
                <div class="col">
                    <h4>Comments</h4>
                    <div class="comment" v-for="comment in user.comments">
                        <div>
                            <p>{{comment.body}}</p>
                            <h5>{{comment.pub_data}}</h5>
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
                username: '1'
            }
        }
    },
    components: {myHeader}
}
</script>
