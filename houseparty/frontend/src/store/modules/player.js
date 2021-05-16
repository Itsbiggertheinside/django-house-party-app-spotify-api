import axios from "axios"
import Vue from 'vue'
import { base_url } from "../config"


export default {

    state: {

        skipper: {},
        skip_votes: [],
        playlists: [],
        tracks: [],
        current_playlist: ''

    },

    mutations: {

        setSkipper(state, payload) {
            state.skipper = payload
        },

        setSkipVote(state, payload) {
            state.skip_votes = payload
        },

        updateSkipVote(state, payload) {
            state.skip_votes.push(payload)
        },

        setRoomPlaylists(state, payload) {
            state.playlists = payload
        },

        setCurrentPlaylist(state, payload) {
            state.current_playlist = payload
        },

        setCurrentPlaylistTracks(state, payload) {
            state.tracks = payload
        }

    },

    actions: {
        
        async increaseSkipVote(state, code) {

            const response = await axios.post(base_url + '/websocket/real-time/', {
                action: 'vote',
                code: code,
            }, { 
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('token')
                } 
            })

            state.commit('setSkipper', response.data)

        },

        async choosePlaylist(state, {code, playlist}) {
            
            const response = await axios.post(base_url + '/websocket/real-time/', {
                action: 'playlist',
                code: code,
                playlist: playlist
            }, {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('token')
                }
            })

            console.log(state.getters.getCurrentPlaylist)
            return response.data

        },

        async playerManager(state, { code, type, playlist='' }) {

            const response = await axios.get(base_url + '/spotify/player/?code=' + code + '&type=' + type + '&playlist=' + playlist, { 
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('token')
                } 
            })

            if (type == 'playlists') {
                state.commit('setRoomPlaylists', response.data.items)
            } else if (type == 'tracks') {
                state.commit('setCurrentPlaylistTracks', response.data.items)
            }

        }

    },

    getters: {

        getSkipVotes: state => state.skip_votes,
        getPlaylists: state => state.playlists,
        getCurrentPlaylist: state => state.current_playlist,
        getTracks: state => state.tracks

    }

}