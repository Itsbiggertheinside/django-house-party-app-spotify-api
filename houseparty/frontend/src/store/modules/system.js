// import axios from 'axios'


export default {

    state: {

        system_information: { message: '', is_visible: false },
        componentKey: 0

    },

    mutations: {

        setSystemInformation(state, payload) {
            state.system_information = payload
        },

        increaseComponentKey(state, payload) {
            state.componentKey += payload
        }

    },

    actions: {

        pushSystemInformation(state, info) {
            const system_info = {
                message: info, 
                is_visible: true
            }
            state.commit('setSystemInformation', system_info)
        }
        
    },

    getters: {

        getSystemInformation: state => state.system_information,
        getComponentKey: state => state.componentKey
        
    }

}