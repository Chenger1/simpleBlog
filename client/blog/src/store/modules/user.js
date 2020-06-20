import axios from 'axios'

const state ={
    user: null,
    token: null
}

const getters = {

}

const mutations ={
    LOGIN_USER: (state, payload)=>{
        state.user ={
            username: payload.username,
            id: payload.id
        }
        localStorage.setItem('user', JSON.stringify(payload))
        state.token = 'Bearer'+payload.token;
        console.log(state.user)
        console.log(payload)
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
                console.log(response)
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