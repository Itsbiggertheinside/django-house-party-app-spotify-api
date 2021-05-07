import axios from 'axios'
import Vue from 'vue'

export default {

    actions: {

        async setCurrentUser(state) {

            const token = state.getters.getToken
            console.log(token)

            const response = await axios.get('http://127.0.0.1:8000/rest-auth/user/', {
                headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': `Token ${token}`
                }
            })

            Vue.$cookies.set('token', token)
            Vue.$cookies.set('username', response.data.username)

            return response.status

        },

    }

}