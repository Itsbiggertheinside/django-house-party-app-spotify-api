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
                <chat :listeners="getListeners"></chat>
            </b-col>
            <b-img fluid 
                style="opacity: .9; position: absolute; width: 30rem; height: auto; left: 0; z-index: 0;" 
                :src="require('../assets/images/cherry-musician.png')" />
        </b-row>

        <settings-modal></settings-modal>
        <div v-show="show_loader" class="room-loader-bg">
            <b-img class="room-loader" :src="require('../assets/images/audio-spectrum.gif')" />
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import Chat from '../components/room/Chat.vue'
import Player from '../components/room/Player.vue'
import Playlist from '../components/room/Playlist.vue'
import SettingsModal from '../components/modals/room/settings/Menu.vue'

export default {
    name: 'Room',
    components: {
        Player, Playlist, Chat, SettingsModal
    },
    methods: {
        ...mapActions({setRoomDetail: 'setRoomDetail', connection: 'createWebSocketConnection', setListener: 'setListener', playerManager: 'playerManager'})
    },
    computed: {
        ...mapGetters({currentRoom: 'getCurrentRoom', getListeners: 'getListeners', getCurrentPlaylist: 'getCurrentPlaylist'})
    },
    data() {
        return {
            code: this.$route.params.code,
            show_loader: true
        }
    },
    async mounted() {
        await this.setRoomDetail(this.code)
        .then(async () => {
            await this.connection(this.code)
            await this.setListener({code: this.code, action_type: 'add'})
            await this.playerManager({code: this.code, type: 'tracks', playlist: this.getCurrentPlaylist})
            .then(() => this.show_loader = false)
        })
    }
}
</script>

<style scoped>

</style>