import axios from 'axios';

const state = {
    posts: {
        '1':{
            'title':'title',
            'body':'body',
            'pub_data': '1'
        }
    },
}

const getters = {
    GET_POSTS_GETTER: (state)=>{
        return state.posts
    },
}

const mutations = {
    SET_POSTS_MUT: (state, payload)=>{
        state.posts = payload
    },
    ADD_POST: (state, payload) =>{
        state.posts.push(payload);
    }
}

const actions = {
    GET_POSTS: async(context, payload)=>{
        let {data} = await axios.get('http://localhost:8000/')
        context.commit('SET_POSTS_MUT', data)   
    }
}


export default{
    state,
    getters,
    mutations,
    actions,
}