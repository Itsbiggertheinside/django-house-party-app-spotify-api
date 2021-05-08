import axios from 'axios'
import { base_url } from '../config'

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
            const response = await axios.post(base_url + '/rest-auth/login/', {
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
            const response = await axios.post(base_url + '/rest-auth/registration/', {
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