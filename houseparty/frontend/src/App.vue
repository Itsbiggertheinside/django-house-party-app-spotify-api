<template>
  <div id="app">
    <div id="nav">
      <navbar></navbar>
    </div>
    <b-container>
      <router-view/>
    </b-container>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import Navbar from "./components/partials/Navbar.vue"

export default {
  components: {
    Navbar
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
