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
import Navbar from "./components/partials/Navbar.vue"

export default {
  components: {
    Navbar
  }
}
</script>


<style>

</style>
