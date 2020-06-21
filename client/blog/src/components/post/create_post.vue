<template>
    <div>
        <my-header></my-header>
        <div class="wrapper">
            <form>
                <div class="form-group">
                    <label for="postTitle">Title</label>
                    <input v-model="post.title" type="text"
                    class="form-control" id="postTitle">
                </div>
                <div class="form-group">
                    <label for="postBody">Body</label>
                    <input v-model="post.body" type="text"
                    class="form-control" id="postBody">
                </div>
                <button v-on:click="submitPost" 
                type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
</template>
<script>
import myHeader from '../header'
export default {
    name: 'createPost',
    data(){
        return{
            post:{
                title: null,
                body: null
            }
        }
    },
    components: {myHeader},
    methods: {
        submitPost(){
            if (this.post.title == null ||
                this.post.body == null){
                    alert('Wrong. Try again')
                } else {
                    this.$store.dispatch('CREATE_POST', this.post);
                    this.$router.push({name: 'HomePage'})
                }
        }
    }
}
</script>