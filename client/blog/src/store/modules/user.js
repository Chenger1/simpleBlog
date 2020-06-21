import axios from 'axios'

const state ={
    local_user_info: {
        username: '',
        id: null,
        is_login: false
    },
    user: null,
    token: null,

}

const getters = {
    IS_AUTH: (state)=>{
        return state.local_user_info.is_login
    },
    GET_USER_INFO: (state)=>{
        return state.user
    },
    GET_USERNAME: (state)=>{
        return state.local_user_info.username
    }
}

const mutations ={
    LOGIN_USER: (state, payload)=>{
        state.local_user_info ={
            username: payload.username,
            id: payload.id,
            is_login: true
        }
        state.token = 'Bearer '+payload.token;
        console.log(payload)
        localStorage.setItem('user', JSON.stringify(payload));
    },
    LOGOUT: (state, payload)=>{
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        location.reload()
    },
    SET_USER_INFO: (state, payload)=>{
        state.user = payload
    }
}

const actions ={
    SAVE_USER: async(context, payload)=>{
        await axios.post('http://127.0.0.1:5000/registration', payload)
        .then((response)=>{
            if(response.status==200){
               console.log(response)
            }
        })
        .catch((error)=>{
            console.log(error)
        })
    },
    USER_LOGIN: async(context, payload)=>{
        await axios.post('http://127.0.0.1:5000/login', payload)
        .then((response)=>{
            if(response.status==200){
                let payloadData = {
                    username: payload.username,
                    id: response.data.id,
                    token: response.data.access_token
                };
                context.commit('LOGIN_USER', payloadData)
            }
        })
    },
    LOGOUT_USER: ({commit})=>{
        commit('LOGOUT');
    },
    GET_USER_DATA: async(context, payload)=>{
        await axios.get('http://127.0.0.1:5000/user_info/'+payload)
        .then((response)=>{
            if(response.status==200){
                context.commit('SET_USER_INFO', response.data)
            }
        })
    }
}

export default{
    state,
    getters,
    mutations,
    actions
}