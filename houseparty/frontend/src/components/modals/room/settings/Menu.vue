<template>
    <div>
        <b-modal id="room-settings-modal" centered>

            <template #modal-header>
                <h5 class="m-0">Ayarlar Menüsü</h5>
                <b-button @click="hideRoomSettingsModal()" class="modal-close-button"><b-icon-x></b-icon-x></b-button>
            </template>

                <b-button v-b-modal.general-settings-modal class="panel-button w-100 my-2"><b-icon-gear class="mx-2" font-scale="1"></b-icon-gear><h6 class="d-inline">Genel Ayarlar</h6></b-button>
                <b-button v-b-modal.playlist-settings-modal class="panel-button w-100 my-2"><b-icon-card-checklist class="mx-2" font-scale="1"></b-icon-card-checklist><h6 class="d-inline">Listeyi Belirle</h6></b-button>

            <template #modal-footer>
                <b-button @click="hideRoomSettingsModal()" class="panel-button"><b-icon-check></b-icon-check></b-button>
            </template>

        </b-modal>
        
        <general-settings></general-settings>
        <playlist-settings></playlist-settings>
    </div>
</template>

<script>
import GeneralSettings from './General.vue'
import PlaylistSettings from './Playlist.vue'

export default {
    components: {
        GeneralSettings, PlaylistSettings
    },
    methods: {
        hideRoomSettingsModal() {
            this.$bvModal.hide('room-settings-modal')
        }
    },
    data() {
        return {
            
        }
    }
}
</script>

<style>

</style>