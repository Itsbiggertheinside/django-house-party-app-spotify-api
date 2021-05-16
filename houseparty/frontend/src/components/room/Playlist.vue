<template>
    <div>
        <b-list-group id="playlist-group">
            <b-list-group-item v-for="tracks in getTracks" :key="tracks.track.id" class="d-flex justify-content-between align-items-center">
                <div class="d-flex justify-content-start align-items-center">
                    <b-avatar class="align-center" square :src="tracks.track.album.images[0].url"></b-avatar>
                    <div class="mx-3">
                        <span>{{tracks.track.album.artists[0].name}} - </span>
                        <span>{{tracks.track.name}}</span>
                    </div>
                </div>
                <span class="mx-3">{{convertDurationToMinutes(tracks.track.duration_ms)}}</span>
            </b-list-group-item>
        </b-list-group>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'


export default {

    methods: {
        convertDurationToMinutes(milliseconds) {
            let minutes = Math.floor(milliseconds / 60000)
            let seconds = ((milliseconds % 60000) / 1000).toFixed(0)
            return seconds == 60 ? (minutes+1) + ":00" : minutes + ":" + (seconds < 10 ? "0" : "") + seconds
        }
    },

    computed: {
        ...mapGetters({getTracks: 'getTracks'})
    }

}
</script>

<style scoped>

    .list-group-item {
        filter: drop-shadow(.2rem .2rem .5rem #075f6e88);
        background-color: #3085ac9d;
        font-weight: 500;
        color: white;
    }

</style>