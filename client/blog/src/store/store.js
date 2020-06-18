import Vue from 'vue';
import Vuex from 'vuex';
import posts from './modules/posts'


Vue.use(Vuex);

export const store = new Vuex.Store({
    modules: {
        posts,
    }
})