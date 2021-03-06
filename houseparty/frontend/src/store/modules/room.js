import Vue from 'vue'
import axios from 'axios'
import { base_url } from '../config'


export default {

    state: {

        active_rooms: [],
        current_room: {},


    },

    mutations: {

        setRooms(state, payload) {
            state.active_rooms = payload
        },

        updateActiveRooms(state, payload) {
            state.active_rooms.push(payload)
        },

        setCurrentRoom(state, payload) {
            state.current_room = payload
        }

    },

    actions: {

        async setRooms(state) {

            const response = await axios.get(base_url + '/api/rooms/', {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('houseparty_token')
                }
            })

            state.commit('setRooms', response.data)

        },

        async setRoomsForAnonymousUsers(state) {

            const response = await axios.get(base_url + '/api/rooms/', {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8'
                }
            })

            state.commit('setRooms', response.data)

        },

        async setRoomDetail(state, code) {

            const response = await axios.get(base_url + '/api/rooms/' + code + '/', {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('houseparty_token')
                }
            })

            state.commit('setCurrentRoom', response.data)
            state.commit('setSkipVote', response.data.player.skip_votes)
            state.commit('setRoomListeners', response.data.listener.active_users)
            state.commit('setCurrentPlaylist', response.data.player.current_playlist)
            state.commit('setCurrentSong', response.data.player.current_song)

        },
        
        async createRoom(state, settings) {

            const response = await axios.post(base_url + '/api/rooms/', {
                code: settings.code,
                guest_can_pause: settings.guest_can_pause,
                votes_to_skip: settings.votes_to_skip_count,
                is_locked: settings.is_locked
            }, { headers: {
                'Accept': 'application/json, */*',
                'Content-Type': 'application/json; charset=utf-8',
                'Authorization': 'Token ' + Vue.$cookies.get('houseparty_token')
            } })

            state.commit('updateActiveRooms', response.data)

            return response.status

        }

    },

    getters: {

        getRooms: state => state.active_rooms,
        getCurrentRoom: state => state.current_room
        
    }

}