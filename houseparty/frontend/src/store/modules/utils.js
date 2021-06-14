import axios from 'axios'
import Vue from 'vue'
import { base_url } from '../config'


export default {

    actions: {

        async setCurrentUser(state) {

            const token = state.getters.getToken
            console.log(token)

            const response = await axios.get(base_url + '/rest-auth/user/', {
                headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': `Token ${token}`
                }
            })

            Vue.$cookies.set('houseparty_token', token)
            Vue.$cookies.set('username', response.data.username)

            return response.status

        },

    }

}