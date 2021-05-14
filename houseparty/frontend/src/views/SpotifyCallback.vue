<template>
    <div>

    </div>
</template>

<script>
export default {
    name: 'SpotifyCallback',
    mounted() {
        let spotify_auth_code = window.location.href.split('=')[1]

        if (spotify_auth_code) {
            // alert(spotify_auth_code)
            window.opener.spotifyCallback(spotify_auth_code)
        }
    }
}
</script>

<style>

</style>