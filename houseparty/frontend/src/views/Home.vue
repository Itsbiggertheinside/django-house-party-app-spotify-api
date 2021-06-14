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
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Home',
  components: {
    RoomList, RoomFilter
  },
  methods: {
    ...mapActions({closeSocket: 'closeSocket', setListener: 'setListener'})
  },
  computed: {
    ...mapGetters({componentKey: 'getComponentKey'})
  },
  async mounted() {
    this.$store.commit('increaseComponentKey', 1)
    try {
      const current_room = this.$store.getters.getCurrentRoom
      if (current_room) {
        await this.setListener({code: current_room.code, action_type: 'remove'})
        .then(async () => {
          await this.closeSocket()
          this.$store.commit('setCurrentRoom', null)
        })
      }
    } catch (e) {
      console.log(e)
    }
  }
}
</script>
