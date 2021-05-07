import axios from 'axios'


export default {

    state: {

        token: ''

    },

    mutations: {

        setToken(state, payload) {
            state.token = payload
        }

    },

    actions: {
        
        async login(state, credentials) {
            const response = await axios.post('http://127.0.0.1:8000/rest-auth/login/', {
                username: credentials.username,
                password: credentials.password
            }, { 
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8'
                } 
            })

            await state.commit('setToken', response.data.key)
        },

        async register(state, credentials) {
            const response = await axios.post('http://127.0.0.1:8000/rest-auth/registration/', {
                username: credentials.username,
                email: credentials.email,
                password1: credentials.password1,
                password2: credentials.password2
            }, { 
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8'
                } 
            })

            await state.commit('setToken', response.data.key)
        },

    },

    getters: {
        
        getToken: state => state.token

    }

}