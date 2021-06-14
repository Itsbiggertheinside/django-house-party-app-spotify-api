import axios from 'axios'
import Vue from 'vue'
import { base_url } from '../config'


export default {

    state: {

        sended_message: {},
        messages: []

    },

    mutations: {

        setSendedMessage(state, payload) {
            state.sended_message = payload
        },

        clearMessages(state, payload) {
            state.messages = payload
        },

        setMessages(state, payload) {
            state.messages.push(payload)
        }

    },

    actions: {

        clearRoomMessages(state) {
            state.commit('clearMessages', [])
        },

        async sendMessage(state, data) {

            let random_id = Math.floor(Math.random() * 712637128)
            
            const response = await axios.post(base_url + '/websocket/real-time/', {
                action: 'chat',
                code: data.code,
                id: random_id,
                text: data.text
            }, {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('houseparty_token')
                }
            })

            state.commit('setSendedMessage', response.data)

        }

    },

    getters: {
        
        getMessages: state => state.messages

    }

}