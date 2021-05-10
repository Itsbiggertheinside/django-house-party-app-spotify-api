<template>
  <div class="home">
    <b-container>
      <b-row>
        <b-col cols="12" class="d-flex justify-content-between align-items-center">
          <b-img style="width: 80px; height: auto;" :src="require('../assets/images/house-party-logo.png')" />
          <div>
            <b-button class="panel-button ml-3" v-b-modal.room-join-modal v-b-tooltip.hover.bottom title="Odaya Katıl">
              <b-icon-door-open-fill></b-icon-door-open-fill>
            </b-button>
            <b-button class="panel-button ml-3" v-b-modal.room-create-modal v-b-tooltip.hover.bottom title="Oda Oluştur">
              <b-icon-hdd-network-fill></b-icon-hdd-network-fill>
            </b-button>
          </div>
        </b-col>
        <b-col cols="12" class="my-4">
          <RoomFilter />
        </b-col>
        <b-col cols="12">
          <RoomList />
        </b-col>
      </b-row>
    </b-container>

    <join></join>
    <create></create>
  </div>
</template>

<script>
import RoomList from '../components/home/RoomList.vue'
import RoomFilter from '../components/home/RoomFilter.vue'
import Join from '../components/modals/room/Join.vue'
import Create from '../components/modals/room/Create.vue'
import { mapActions } from 'vuex'

export default {
  name: 'Home',
  components: {
    RoomList, RoomFilter, Join, Create
  },
  methods: {
    ...mapActions({closeSocket: 'closeSocket'})
  },
  mounted() {
    this.closeSocket()
  }
}
</script>
