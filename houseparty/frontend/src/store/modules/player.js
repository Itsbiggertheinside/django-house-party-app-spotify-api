import axios from "axios"
import Vue from 'vue'
import { base_url } from "../config"


export default {

    state: {

        skipper: {},
        skip_votes: [],
        playlists: [],
        tracks: [],
        current_playlist: '',
        current_song: ''

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

        setCurrentSong(state, payload) {
            state.current_song = payload
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
                    'Authorization': 'Token ' + Vue.$cookies.get('houseparty_token')
                } 
            })

            state.commit('setSkipper', response.data)

        },

        async choosePlaylist(state, {code, playlist}) {
            
            const response = await axios.post(base_url + '/websocket/real-time/', {
                action: 'playlist',
                code: code, playlist: playlist
            }, {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('houseparty_token')
                }
            })

            console.log(state.getters.getCurrentPlaylist)
            return response.data

        },

        async setCurrentSong(state, {code, song}) {

            const response = await axios.post(base_url + '/websocket/real-time/', {
                action: 'currently_playing',
                code: code, song: song
            }, {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('houseparty_token')
                }
            })

            console.log(state.getters.getCurrentSong)
            return response.data

        },

        async playSong(state, {code, playlist: playlist, song}) {

            const response = await axios.post(base_url + '/websocket/real-time/', {
                action: 'play_song',
                code: code, playlist: playlist, song: song
            }, {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('houseparty_token')
                }
            })

            console.log(state.getters.getCurrentSong)
            return response.data

        },

        async playerManager(state, { code, type, playlist='', song_offset='' }) {

            const response = await axios.get(base_url + '/spotify/player/?code=' + code + '&type=' + type + '&playlist=' + playlist + '&song_offset=' + song_offset, { 
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('houseparty_token')
                } 
            })

            if (type == 'playlists') {
                state.commit('setRoomPlaylists', response.data.items)
            } else if (type == 'tracks') {
                state.commit('setCurrentPlaylistTracks', response.data.items)
            } else if (type == 'play_song') {
                state.commit('setCurrentSong', response.data)
                state.dispatch('setCurrentSong', { code: code, song: response.data.track_name })
            }

        }

    },

    getters: {

        getSkipVotes: state => state.skip_votes,
        getPlaylists: state => state.playlists,
        getCurrentPlaylist: state => state.current_playlist,
        getCurrentSong: state => state.current_song,
        getTracks: state => state.tracks

    }

}