import axios from 'axios'

const state ={
    user: null,
    token: null
}

const getters = {
    IS_AUTH: (state)=>{
        return !!state.user
    }
}

const mutations ={
    LOGIN_USER: (state, payload)=>{
        state.user ={
            username: payload.username,
            id: payload.id
        }
        state.token = 'Bearer'+payload.token;
        localStorage.setItem('user', JSON.stringify(payload));
    },
    LOGOUT: (state, payload)=>{
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        location.reload()
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
    }
}

export default{
    state,
    getters,
    mutations,
    actions
}