<template>
  <div class="home">
    <b-container>
      <b-row>
        <b-col cols="12" class="my-4">
          <RoomFilter />
        </b-col>
        <b-col cols="12">
          <RoomList />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import RoomList from '../components/home/RoomList.vue'
import RoomFilter from '../components/home/RoomFilter.vue'
import { mapActions } from 'vuex'

export default {
  name: 'Home',
  components: {
    RoomList, RoomFilter
  },
  methods: {
    ...mapActions({closeSocket: 'closeSocket', setListener: 'setListener'})
  },
  async mounted() {
    try {
      const current_room_code = this.$store.getters.getCurrentRoom.code
      if (current_room_code) {
        await this.setListener({code: current_room_code, action_type: 'remove'})
        .then(async () => {
          await this.closeSocket()
          this.$store.commit('increaseComponentKey', 1)
        })
      }
    } catch (e) {
      console.log(e)
    }
  }
}
</script>
