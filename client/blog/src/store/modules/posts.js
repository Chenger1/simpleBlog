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
    GET_POST_DATA: (state)=>(id)=>{
        let post_index = state.posts.findIndex(post=>post.id==id);
        return state.posts[post_index]
    },
}

const mutations = {
    SET_POSTS_MUT: (state, payload)=>{
        state.posts = payload
    },
    ADD_POST: (state, payload) =>{
        state.posts.push(payload);
    },
    EDIT_POST_MUTATION: (state, payload)=>{
        let post_index = state.posts.findIndex(post=>post.id==payload.id);
        state.posts[post_index]['title'] = payload.title;
        state.posts[post_index]['body'] = payload.body; 
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
    EDIT_POST: async(context, payload)=>{
        await axios.patch('http://127.0.0.1:5000/edit_post/'+payload.id, payload, {headers:{'Authorization': context.rootState.user.token}})
        .then((response)=>{
            context.commit('EDIT_POST_MUTATION', payload)
        })
    },
    DELETE_POST: async(context, payload)=>{
        await axios.post('http://127.0.0.1:5000/delete_post/'+payload.post.id, payload, {headers:{'Authorization': context.rootState.user.token}})
    },
    CREATE_COMMENT: async(context, payload)=>{
        await axios.post('http://127.0.0.1:5000/create_comment/'+payload['comment_id'], payload['payload'], {headers:{'Authorization': context.rootState.user.token}})
        .then((response)=>{
            if(response.status == 201){
                console.log(response)
            }
        })
    },
    EDIT_COMMENT: async(context, payload)=>{
        payload['username'] = context.rootState.user.local_user_info.username;
        await axios.patch('http://127.0.0.1:5000/edit_comment/'+payload.id, payload, {headers:{'Authorization': context.rootState.user.token}})
    },
    DELETE_COMMENT: async(context, payload)=>{
        await axios.post('http://127.0.0.1:5000/delete_comment/'+payload.comment.id, payload, {headers:{'Authorization': context.rootState.user.token}})
    }
}


export default{
    state,
    getters,
    mutations,
    actions,
}