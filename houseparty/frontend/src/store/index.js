import Vue from 'vue'
import Vuex from 'vuex'

import auth from './modules/auth'
import room from './modules/room'
import profile from './modules/profile'
import utils from './modules/utils'

Vue.use(Vuex)

export default new Vuex.Store({
  
  strict: true,

  modules: {
    auth, room, profile, utils
  }

})
