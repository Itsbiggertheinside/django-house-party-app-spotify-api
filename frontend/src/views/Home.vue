<template>
  <div class="home">
    <b-container>
      <b-row>
        <b-col cols="12">
          <b-row align-h="between" align-v="center">
            <h1>Oda Listesi</h1>
            <div>
              <b-button squared variant="outline-info" class="ml-3">Odaya Katıl</b-button>
              <b-button squared variant="outline-info" class="ml-3">Oda Oluştur</b-button>
            </div>
          </b-row>
        </b-col>
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

export default {
  name: 'Home',
  components: {
    RoomList, RoomFilter
  }
}
</script>
