<template>
    <div class="room-retrieve">
        <b-row class="mt-3 mb-5" align-h="around">
            <b-col md="5">
                <b-row>
                    <b-col cols="12" class="mb-4" style="z-index: 1;">
                        <player :player_data="currentRoom"></player>
                    </b-col>
                    <b-col cols="12" class="mb-4" style="z-index: 1;">
                        <playlist></playlist>
                    </b-col>
                </b-row>
            </b-col>
            <b-col md="7" style="z-index: 1;">
                <chat></chat>
            </b-col>
            <b-img fluid 
                style="opacity: .9; position: absolute; width: 30rem; height: auto; left: 0; z-index: 0;" 
                :src="require('../assets/images/cherry-musician.png')" />
        </b-row>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import Chat from '../components/room/Chat.vue'
import Player from '../components/room/Player.vue'
import Playlist from '../components/room/Playlist.vue'

export default {
    name: 'Room',
    components: {
        Player, Playlist, Chat 
    },
    methods: {
        ...mapActions({setRoomDetail: 'setRoomDetail', connection: 'createWebSocketConnection', closeSocket: 'closeSocket'})
    },
    computed: {
        ...mapGetters({currentRoom: 'getCurrentRoom'})
    },
    data() {
        return {
            code: this.$route.params.code
        }
    },
    async mounted() {
        await this.setRoomDetail(this.code)
        .then(async () => {
            await this.connection(this.code)
        })
    }
}
</script>

<style scoped>

</style>