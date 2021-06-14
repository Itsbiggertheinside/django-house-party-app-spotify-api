import axios from 'axios'
import Vue from 'vue'
import { base_url } from '../config'


export default {

    state: {

        listener: {},
        listeners: []

    },

    mutations: {

        setRoomListeners(state, payload) {
            state.listeners = payload
        },

        increaseRoomListeners(state, payload) {
            state.listeners.push(payload)
        },

        decreaseRoomListeners(state, payload) {
            state.listeners.pop(payload)
        }

    },

    actions: {

        async setListener(state, {code, action_type}) {

            const response = await axios.post(base_url + '/websocket/real-time/', {
                action: 'listening',
                code: code,
                action_type: action_type
            }, { 
                headers: {
                'Accept': 'application/json, */*',
                'Content-Type': 'application/json; charset=utf-8',
                'Authorization': 'Token ' + Vue.$cookies.get('houseparty_token')
                } 
            })

            console.log(state)
            console.log(response.data)

        }
        
    },

    getters: {
        getListeners: state => state.listeners
    }

}