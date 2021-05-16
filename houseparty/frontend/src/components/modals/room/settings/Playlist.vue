<template>
    <div>
        <b-modal id="playlist-settings-modal" centered>

            <template #modal-header>
                <h5 class="m-0">Playlist Seçimi</h5>
                <b-button @click="hideRoomPlaylistSettingsModal()" class="modal-close-button"><b-icon-x></b-icon-x></b-button>
            </template>

            <b-list-group>
                <b-list-group-item @click="handleChoosePlaylist(playlist.id)" v-for="playlist in getPlaylists" :key="playlist.id" class="d-flex justify-content-between align-items-center">
                    <div>
                        <b-avatar square :src="playlist.images[0].url"></b-avatar>
                        <span class="m-3">{{playlist.name}}</span>
                    </div>
                    <span class="m-3">{{playlist.tracks.total}} şarkı</span>
                </b-list-group-item>
            </b-list-group>

            <template #modal-footer>
                <b-button @click="hideRoomPlaylistSettingsModal()" class="panel-button"><b-icon-check></b-icon-check></b-button>
            </template>

        </b-modal>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'


export default {
    methods: {
        ...mapActions({playerManager: 'playerManager', choosePlaylist: 'choosePlaylist'}),
        hideRoomPlaylistSettingsModal() {
            this.$bvModal.hide('playlist-settings-modal')
        },
        async handleChoosePlaylist(playlist) {
            await this.choosePlaylist({code: this.room_code, playlist: playlist})
        }
    },
    computed: {
        ...mapGetters({getPlaylists: 'getPlaylists'})
    },
    data() {
        return {
            room_code: this.$route.params.code
        }
    },
    async mounted() {
        await this.playerManager({code: this.room_code, type: 'playlists'})
        .then(() => console.log('ok'))
        .catch(err => console.log(err))
    }
}
</script>

<style scoped>

    .list-group-item {
        background-color: #102B4C;
        font-weight: 500;
        color: white;
        cursor: pointer;
    }

    .list-group-item:hover {
        filter: drop-shadow(.2rem .2rem .5rem #000000);
        background-color: #111111;
    }

</style>