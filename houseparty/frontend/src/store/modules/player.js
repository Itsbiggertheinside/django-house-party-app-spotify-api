import axios from "axios"
import Vue from 'vue'
import { base_url } from "../config"


export default {

    state: {

        skipper: {},
        skip_votes: []

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

        }

    },

    getters: {

        getSkipVotes: state => state.skip_votes

    }

}