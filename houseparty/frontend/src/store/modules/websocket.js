import { websocket_url } from '../config'


export default {

    state: {

        socket: '',

    },

    mutations: {

        setWebSocket(state, payload) {
            state.socket = payload
        },

    },

    actions: {

        closeSocket(state) {
            const socket = state.getters.getWebSocket
            socket.close()
        },
        
        createWebSocketConnection(state, code) {
        
            const socket = new WebSocket(websocket_url + '/ws/room/' + code + '/')
            state.commit('setWebSocket', socket)
        
            socket.onmessage = ({data}) => {
                    
                let websocket_data = JSON.parse(data)
                console.log(websocket_data)

                // -----------------------------------------------

                if (websocket_data.action == 'chat') {

                    state.commit('setMessages', websocket_data)

                } 
                
                else if (websocket_data.action == 'vote') {

                    if (!state.getters.getSkipVotes.some(data => data.user_id == websocket_data.user_id)) {
                        state.commit('updateSkipVote', websocket_data)
                    } else {
                        console.log('Zaten bir oyda bulundun!')
                    }

                }

                else if (websocket_data.action == 'listening') {
                    
                    console.log('listening data:', websocket_data)
                    
                    if (websocket_data.action_type == 'add') {
                        
                        if(!state.getters.getListeners.some(data => data.user_id == websocket_data.user_id)) {
                            state.commit('increaseRoomListeners', websocket_data)
                        }

                    } else if (websocket_data.action_type == 'remove') {

                        state.commit('decreaseRoomListeners', websocket_data)

                    }

                }

                else if (websocket_data.action == 'playlist') {

                    state.dispatch('playerManager', { code: websocket_data.code, type: 'tracks', playlist: websocket_data.playlist })

                }

                else if (websocket_data.action == 'play_song') {

                    state.dispatch('playerManager', { code: websocket_data.code, type: 'play_song', playlist: websocket_data.playlist, song_offset: websocket_data.song })
                    
                }

                // -----------------------------------------------
        
            }
        
        },

    },

    getters: {
        getWebSocket: state => state.socket,
    }

}