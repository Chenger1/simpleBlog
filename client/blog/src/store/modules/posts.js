import axios from 'axios';

const state = {
    posts: {
        '1':{
            'title':'title',
            'body':'body',
            'pub_data': '1',
            'comments': [
                {
                    'author':'User',
                    'body':'comment',
                    'pub_data':'21'
                }
            ]
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
        let {data} = await axios.get('http://127.0.0.1:5000/')
        context.commit('SET_POSTS_MUT', data['resp'])   
    }
}


export default{
    state,
    getters,
    mutations,
    actions,
}