import axios from 'axios'

const state ={
    user: null,
    token: null
}

const getters = {

}

const mutations ={

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
    }
}

export default{
    state,
    getters,
    mutations,
    actions
}