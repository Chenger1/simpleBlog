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
                <button v-on:click="editPost" 
                type="button" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
</template>
<script>
import myHeader from '../header'
export default {
    name: 'editPost',
    data(){
        return {
            post:{}
        }
    },
    components: {myHeader},
    methods: {
        editPost(){
            this.$store.dispatch('EDIT_POST', this.post);
            this.$router.push({name: 'HomePage'});
        }
    },
    mounted(){
        this.post = this.$store.getters.GET_POST_DATA(this.$route.params.id)
    }
}
</script>