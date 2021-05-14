import Vue from 'vue'
import axios from 'axios'
import { base_url } from '../config'


export default {

    state: {

        spotify_authentication_url: '',
        spotify_callback_data: {},
        spotify_is_connected: false

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

        }

    },

    getters: {

        getSpotifyAuthenticationUrl: state => state.spotify_authentication_url,
        getSpotifyCallbackData: state => state.spotify_callback_data,
        getSpotifyIsConnected: state => state.spotify_is_connected
        
    }

}