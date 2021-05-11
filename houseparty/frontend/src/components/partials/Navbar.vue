<template>
    <div>
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
            <b-button v-if="is_authenticated" class="panel-button ml-3" v-b-modal.room-create-modal v-b-tooltip.hover.bottom title="Oda Oluştur">
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
export default {
    methods: {
        handleRoute(link) {
            if (link == '/login') {
                this.$cookies.remove('token')
                this.$cookies.remove('username')
                window.location.href = '/login'
            } else {
                this.$router.push(link)
            }
        }
    },
    data() {
        return {
            is_authenticated: this.$cookies.isKey('token')
        }
    }
}
</script>

<style>

</style>