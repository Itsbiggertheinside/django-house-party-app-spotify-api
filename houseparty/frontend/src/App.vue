<template>
  <div id="app">
    <b-container>
      <b-col cols="12" class="d-flex justify-content-end align-items-center mb-4">
        <navbar></navbar>
      </b-col>
      <router-view/>
    </b-container>


    <join></join>
    <create></create>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import Navbar from "./components/partials/Navbar.vue"
import Join from './components/modals/room/Join.vue'
import Create from './components/modals/room/Create.vue'

export default {
  components: {
    Navbar, Join, Create
  },
  methods: {
    ...mapActions(['setRooms'])
  },
  mounted() {
    this.setRooms()
  }
}
</script>


<style>

</style>
