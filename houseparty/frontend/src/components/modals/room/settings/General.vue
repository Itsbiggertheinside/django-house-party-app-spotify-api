<template>
    <div>
        <b-modal id="general-settings-modal" centered>

            <template #modal-header>
                <h5 class="m-0">Genel Ayarlar</h5>
                <b-button @click="hideRoomGeneralSettingsModal()" class="modal-close-button"><b-icon-x></b-icon-x></b-button>
            </template>

            <p>Genel ayarlarını düzenle</p>

            <template #modal-footer>
                <b-button @click="hideRoomGeneralSettingsModal()" class="panel-button"><b-icon-check></b-icon-check></b-button>
            </template>

        </b-modal>
    </div>
</template>

<script>
export default {
    methods: {
        hideRoomGeneralSettingsModal() {
            this.$bvModal.hide('general-settings-modal')
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