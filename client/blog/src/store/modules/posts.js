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
    },
    CREATE_POST: async(context, payload)=>{
        payload['user'] = context.rootState.user.local_user_info.username;
        await axios.post('http://127.0.0.1:5000/create_post', payload, {headers:{'Authorization': context.rootState.user.token}})
        .then((response)=>{
            if(response.status == 201){
                console.log(response)
            }
        })
    },
}


export default{
    state,
    getters,
    mutations,
    actions,
}