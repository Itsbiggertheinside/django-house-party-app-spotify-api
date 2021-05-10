import Vue from 'vue'
import Vuex from 'vuex'

import auth from './modules/auth'
import room from './modules/room'
import profile from './modules/profile'
import utils from './modules/utils'
import chat from './modules/chat'
import player from './modules/player'
import websocket from './modules/websocket'

Vue.use(Vuex)

export default new Vuex.Store({
  
  strict: true,

  modules: {
    auth, room, profile, utils, chat, player, websocket
  }

})
