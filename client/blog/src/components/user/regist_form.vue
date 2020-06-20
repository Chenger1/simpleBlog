<template>
    <div>
        <my-header></my-header>
        <div class="wrapper">
           <form>
            <div class="form-group">
                <label for="InputEmail1">Email address</label>
                <input 
                v-model="user.email"
                type="email" class="form-control" 
                id="InputEmail1" aria-describedby="emailHelp"
                >
                <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
            </div>
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
            v-on:click="userReg">Submit</button>
            </form>
            Already have an account? Click
            <router-link to="/login">Login</router-link>
        </div>
    </div>
</template>
<script>
import myHeader from '../header';
export default {
    name: 'registration_form',
    data(){
        return{
            user: {
                username: null,
                email: null,
                password: null
            }
        }
    },
    components: {myHeader},
    methods: {
        userReg() {
            if (
                this.user.username == null ||
                this.user.email == null ||
                this.user.password == null
            ){
                alert('Wrong. Try again')
            } else {
                this.$store.dispatch('SAVE_USER', this.user).then(()=>{
                        this.$router.push({name: 'userLogin'});
                    });
                }
            }
        }
    }
</script>