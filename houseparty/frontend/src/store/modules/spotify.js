import Vue from 'vue'
import axios from 'axios'
import { base_url } from '../config'


export default {

    state: {

        spotify_authentication_url: '',
        spotify_callback_data: {},
        spotify_is_connected: false,
        spotify_is_authenticated: false,
        key_is_available: false

    },

    mutations: {

        setSpotifyAuthenticationUrl(state, payload) {
            state.spotify_authentication_url = payload
        },

        setSpotifyCallbackData(state, payload) {
            state.spotify_callback_data = payload
        },

        setSpotifyIsConnected(state, payload) {
            state.spotify_is_connected = payload
        },

        setSpotifyIsAuthenticated(state, payload) {
            state.spotify_is_authenticated = payload
        },
        
        setSpotifyKeyIsAvailable(state, payload) {
            state.key_is_available = payload
        }

    },

    actions: {

        async setSpotifyAuthenticationUrl(state) {

            const response = await axios.get(base_url + '/spotify/auth-url/', {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('token')
                }
            })

            state.commit('setSpotifyAuthenticationUrl', response.data.url)
        },

        async catchSpotifyCallbackData(state, code) {

            const response = await axios.get(base_url + '/spotify/callback/?code=' + code, {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('token')
                }
            })

            state.commit('setSpotifyCallbackData', response.data)

            if (response.status == 201) {
                state.commit('setSpotifyIsConnected', true)
                // state.dispatch('pushSystemInformation', 'Spotify hesabınız kaydedildi! Hemen bir oda oluşturabilir ve arkadaşlarınla eğlenmeye başlayabilirsiniz.')
            } 
            // else {
            //     state.dispatch('pushSystemInformation', 'Spotify hesabınız kaydedilirken bir sorun oluştu! Şimdilik yalnızca kayıtlı odalara giriş yapabilirsin, ancak dilediğin zaman profilinden spotify ayarlarını düzenleyebilirsin!')
            // }

        },

        async checkSpotifyConnectivity(state) {

            const response = await axios.get(base_url + '/api/control-center/', {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('token')
                }
            })

            state.commit('setSpotifyIsAuthenticated', response.data.spotify_is_authenticated)
            state.commit('setSpotifyKeyIsAvailable', response.data.key_is_available)

        },

        async refreshSpotifyToken(state) {

            const response = await axios.get(base_url + '/spotify/refresh-token/', {
                headers: {
                    'Accept': 'application/json, */*',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Authorization': 'Token ' + Vue.$cookies.get('token')
                }
            })

            console.log(state.getters.getSpotifyKeyIsAvailable)
            return response.status

        }

    },

    getters: {

        getSpotifyAuthenticationUrl: state => state.spotify_authentication_url,
        getSpotifyCallbackData: state => state.spotify_callback_data,
        getSpotifyIsConnected: state => state.spotify_is_connected,
        getSpotifyIsAuthenticated: state => state.spotify_is_authenticated,
        getSpotifyKeyIsAvailable: state => state.key_is_available
        
    }

}