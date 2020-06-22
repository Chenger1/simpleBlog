<template>
    <div>
        <my-header></my-header>
        <div class="wrapper">
            <form>
                <div class="form-group">
                    <label for="postBody">Body</label>
                    <input v-model="comment.body" type="text"
                    class="form-control" id="postBody">
                </div>
                <button v-on:click="submitComment" 
                type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
</template>
<script>
import myHeader from '../header'
export default {
    name: 'createComment',
    data(){
        return {
            comment:{
                body: null
            }
        }
    },
    components: {myHeader},
    methods:{
        submitComment(){
        if (this.comment.body == null){
                alert('Wrong. Try again')
        } else {
            let payload = {
                'payload':{
                    'comment': this.comment,
                    'username': this.get_username
                },
                'comment_id': this.$route.params.id,
            }
            this.$store.dispatch('CREATE_COMMENT', payload);
            this.$router.push({name: 'HomePage'})
            }
        }
    },
    computed: {
        get_username(){
            return this.$store.getters.GET_USERNAME;
        }
    }
}
</script>