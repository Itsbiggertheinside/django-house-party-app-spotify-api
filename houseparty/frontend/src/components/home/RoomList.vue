<template>
    <div id="room-list">
        <b-row>
            <b-col md="6" v-for="room in rooms" :key="room.code">
                <b-card text-variant="white">
                    <b-card-body>
                        <div class="d-flex justify-content-between align-items-center">
                            <div class="d-flex align-items-center">
                                <b-avatar></b-avatar>
                                <h6 class="m-0">{{room.host_username}}</h6>
                            </div>
                            <h4 class="m-0">#{{room.code}}</h4>
                        </div>
                        <div class="divider my-2"></div>
                        <div class="mt-4">
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="d-flex align-items-center">
                                    <b-icon-pause-fill font-scale="2"></b-icon-pause-fill>
                                    <p class="m-0">Weekend - Save Your Tears</p>
                                </div>
                            </div>
                        </div>
                    </b-card-body>
                    <b-card-footer class="d-flex justify-content-between align-items-center">
                        <b-avatar-group size="2rem" v-b-tooltip.hover.bottom title="15 aktif dinleyen">
                            <b-avatar src="https://placekitten.com/300/300" variant="info"></b-avatar>
                            <b-avatar src="https://placekitten.com/320/320" variant="dark"></b-avatar>
                            <b-avatar src="https://placekitten.com/300/300" variant="info"></b-avatar>
                            <b-avatar src="https://placekitten.com/320/320" variant="dark"></b-avatar>
                            <b-avatar src="https://placekitten.com/300/300" variant="info"></b-avatar>
                            <b-avatar src="https://placekitten.com/320/320" variant="dark"></b-avatar>
                        </b-avatar-group>
                        <b-button @click="enterRoom(room.code)" v-b-popover.hover.right title="Odaya Katıl" class="modal-close-button m-0 p-0"><b-icon-play-fill></b-icon-play-fill></b-button>
                    </b-card-footer>
                </b-card>
            </b-col>
        </b-row>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'


export default {
    methods: {
        enterRoom(code) {
            this.$router.push('/room/' + code)
        }
    },
    computed: {
        ...mapGetters({rooms: 'getRooms'})
    }
}
</script>

<style>

</style>