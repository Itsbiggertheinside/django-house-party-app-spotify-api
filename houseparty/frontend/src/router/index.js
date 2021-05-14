import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Auth from '../views/Auth.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Auth',
    component: Auth
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/room/:code',
    name: 'Room',

    component: () => import(/* webpackChunkName: "room" */ '../views/Room.vue')
  },
  {
    path: '/spotify/callback',
    name: 'SpotifyCallback',

    component: () => import(/* webpackChunkName: "spotifyCallback" */ '../views/SpotifyCallback.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
