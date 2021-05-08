// import axios from 'axios'
import { websocket_url } from '../config'


export default {

    state: {

        socket: ''

    },

    mutations: {

        setSocket(state, payload) {
            state.socket = payload
        }

    },

    actions: {
        
        createWebSocketConnection(state, code) {

            const socket = new WebSocket(websocket_url)

        }

    },

    getters: {
        
        getSocket: state => state.socket

    }

}