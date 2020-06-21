<template>
    <div>
        <my-header></my-header>
        <div class="wrapper">
           <form>
            <div class="form-group">
                <label for="inputUsername">Username</label>
                <input 
                v-model="user.username"
                type="text" class="form-control" 
                id="inputUsername">
            </div>
            <div class="form-group">
                <label for="InputPassword1">Password</label>
                <input 
                v-model="user.password"
                type="password" class="form-control" 
                id="InputPassword1">
            </div>
            <button type="submit" class="btn btn-primary"
            v-on:click="userLogin">Submit</button>
            </form>
            Don`t have an acount? Click
            <router-link to="/registration">Registration</router-link>
        </div>
    </div>
</template>
<script>
import myHeader from '../header'
export default {
    name: 'userLogin',
    data(){
        return{
            user:{
                username: null,
                password: null
            }
        }
    },
    components: {myHeader},
    methods: {
        userLogin(){
            if(
                this.user.username == null ||
                this.user.password == null
            ){
                alert('Wrong. Try again')
            } else{
                this.$store.dispatch('USER_LOGIN', this.user).then(()=>{
                    this.$router.push({name: 'userProfile', params:{username: this.user.username}})
                })
            }
        }
    }
}
</script>