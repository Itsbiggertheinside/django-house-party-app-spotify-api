<template>
    <div id="nav">
        <!-- <b-img style="width: 80px; height: auto;" :src="require('../../assets/images/house-party-logo.png')" /> -->
        <div>
            <b-button v-if="!is_authenticated" @click="handleRoute('/login')" class="panel-button ml-3" v-b-tooltip.hover.bottom title="Giriş Yap">
                <b-icon-key-fill></b-icon-key-fill>
            </b-button>
            <b-button @click="handleRoute('/home')" class="panel-button ml-3" v-b-tooltip.hover.bottom title="Ana Sayfa">
                <b-icon-house-door-fill></b-icon-house-door-fill>
            </b-button>
            <b-button v-if="is_authenticated" class="panel-button ml-3" v-b-modal.room-join-modal v-b-tooltip.hover.bottom title="Odaya Katıl">
                <b-icon-door-open-fill></b-icon-door-open-fill>
            </b-button>
            <b-button v-if="is_authenticated" @click="handleRoomCreateModal()" class="panel-button ml-3" v-b-tooltip.hover.bottom title="Oda Oluştur">
                <b-icon-geo-fill></b-icon-geo-fill>
            </b-button>
            <b-button v-if="is_authenticated" @click="handleRoute('/profile')" class="panel-button ml-3" v-b-tooltip.hover.bottom title="Profilim">
                <b-icon-person-fill></b-icon-person-fill>
            </b-button>
            <b-button v-if="is_authenticated" @click="handleRoute('/login')" class="panel-button ml-3" v-b-tooltip.hover.bottom title="Çıkış Yap">
                <b-icon-plug-fill></b-icon-plug-fill>
            </b-button>
        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    methods: {
        ...mapActions({refreshSpotifyToken: 'refreshSpotifyToken'}),
        handleRoute(link) {
            this.$router.push(link)
            this.$store.commit('increaseComponentKey', 1)
        },
        async handleRoomCreateModal() {
            await this.refreshSpotifyToken()
            .then(async () => {
                    this.$bvModal.show('room-create-modal')
                    await this.refreshSpotifyToken()
                    .then(status => {
                        console.log('refresh spotify token status:', status)
                        this.$bvModal.show('room-create-modal')
                    }).catch(err => console.log(err))
            }).catch(err => console.log(err))
        }
    },
    computed: {
        
    },
    data() {
        return {
            is_authenticated: this.$cookies.isKey('houseparty_token')
        }
    }
}
</script>

<style>

</style>