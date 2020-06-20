import Vue from 'vue';
import Vuex from 'vuex';
import posts from './modules/posts'
import user from './modules/user'


Vue.use(Vuex);

export const store = new Vuex.Store({
    modules: {
        posts,
        user,
    }
})