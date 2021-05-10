<template>
    <div>
        <b-modal id="room-join-modal" ref="room-join-modal" centered>

            <template #modal-header>
                <h5 class="m-0">Bir odaya katıl</h5>
                <b-button @click="hideRoomJoinModal()" class="modal-close-button"><b-icon-x></b-icon-x></b-button>
            </template>

            <p class="mt-2 mb-3">Katılmak istediğin odanın eşsiz numarasını gir:</p>
            <b-form-input v-model="room_name" class="my-3"></b-form-input>

            <template #modal-footer>
                <b-button @click="handleEnterRoom(room_name)" class="panel-button"><b-icon-check></b-icon-check></b-button>
            </template>

        </b-modal>
    </div>
</template>

<script>
export default {
    methods: {
        handleEnterRoom(room_name) {
            this.$router.push('/room/' + room_name)
        },
        hideRoomJoinModal() {
            this.$refs['room-join-modal'].hide()
        }
    }
}
</script>

<style>

</style>