<template>
    <div>

    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'SpotifyCallback',
    methods: {
        ...mapActions({ catchSpotifyCallbackData: 'catchSpotifyCallbackData' }),
    },
    computed: {
        ...mapGetters({ getSpotifyIsConnected: 'getSpotifyIsConnected' })
    },
    async mounted() {
        let spotify_auth_code = window.location.href.split('=')[1]

        if (spotify_auth_code) {
            await this.catchSpotifyCallbackData(spotify_auth_code)
            .then(() => {
                if (this.getSpotifyIsConnected) {
                    window.location.href = '/home'
                }
            }).catch(err => console.log(err))
        }
    }
}
</script>

<style>

</style>