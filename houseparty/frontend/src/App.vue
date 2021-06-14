<template>
  <div id="app">
    <b-img id="particule-bg" :src="require('./assets/images/particule-bg.jpg')" />
    <b-container>
      <b-col cols="12" class="d-flex justify-content-end align-items-center mb-4" id="nav">
        <navbar :key="componentKey"></navbar>
      </b-col>
      <router-view/>
    </b-container>


    <join></join>
    <create></create>
    <!-- <system :system_info="systemInformation"></system> -->
  </div>
</template>

<script>
import { 
  mapActions, 
  mapGetters 
} from 'vuex'
import Navbar from "./components/partials/Navbar.vue"
import Join from './components/modals/room/Join.vue'
import Create from './components/modals/room/Create.vue'
// import System from './components/modals/info/System.vue'

export default {
  components: {
    Navbar, Join, Create,
    // System
  },
  methods: {
    ...mapActions(['setRooms', 'setRoomsForAnonymousUsers'])
  },
  computed: {
    ...mapGetters({componentKey: 'getComponentKey'})
  },
  mounted() {
    if (!this.$cookies.get('houseparty_token')) {
      this.setRoomsForAnonymousUsers()
    } else {
      this.setRooms()
    }
  }
}
</script>


<style>

</style>
