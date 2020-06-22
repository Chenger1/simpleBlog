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
                <button v-on:click="editComment" 
                type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
</template>
<script>
import myHeader from '../header'
export default {
    name: 'editComment',
    data(){
        return {
            comment: {
                id: this.$route.params.comment_id,
                body: this.$route.params.body
            }
        }
    },
    components: {myHeader},
    methods: {
        editComment(){
            this.$store.dispatch('EDIT_COMMENT', this.comment);
            this.$router.push({name: 'HomePage'});
        }
    },

}
</script>