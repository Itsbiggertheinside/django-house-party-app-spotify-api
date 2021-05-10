<template>
    <div>
        <b-card text-variant="white">
            <template #header>
                <div class="d-flex justify-content-between align-items-center">
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">{{player_data.host_username}}</p>
                    </div>
                    <h6 class="m-0">#{{player_data.code}}</h6>
                </div>
            </template>
            <b-card-body class="p-1">
                <div class="d-flex justify-content-between align-items-center">
                    <div class="d-flex align-items-center">
                        <b-icon-music-note-beamed class="p-1" font-scale="2"></b-icon-music-note-beamed>
                        <p class="m-0">Weekend - Save Your Tears</p>
                    </div>
                </div>
            </b-card-body>
            <template #footer>
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <b-button @click="handleSkipVote()" v-b-tooltip.hover.bottom="'Şarkıyı geçmek için oyla'" class="modal-close-button p-1"><b-icon-skip-end-fill font-scale="1.8"></b-icon-skip-end-fill></b-button>
                        <span>{{getSkipVotes.length}} oy verildi</span>
                    </div>
                    <div>
                        <b-button v-b-tooltip.hover.bottom="'Sesi kapat'" class="modal-close-button p-2"><b-icon-reception4 font-scale="1.2"></b-icon-reception4></b-button>
                        <b-button v-b-tooltip.hover.bottom="'Şarkıyı paylaş'" class="modal-close-button p-2"><b-icon-share-fill font-scale="1.2"></b-icon-share-fill></b-button>
                        <b-button v-b-tooltip.hover.bottom="'Detayları görüntüle'" class="modal-close-button p-2"><b-icon-info-circle-fill font-scale="1.2"></b-icon-info-circle-fill></b-button>
                    </div>
                </div>
            </template>
        </b-card>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    props: ['player_data'],
    methods: {
        ...mapActions({increaseSkipVote: 'increaseSkipVote'}),
        async handleSkipVote() {
            await this.increaseSkipVote(this.player_data.code)
        }
    },
    computed: {
        ...mapGetters({getSkipVotes: 'getSkipVotes'})
    },
    data() {
        return {
            votes_count: 0
        }
    },
    mounted() {
        
    }
}
</script>

<style scoped>

    .card {
        filter: drop-shadow(.2rem .2rem .5rem #791f1f93);
        background-color: #f32b2bbd !important;
    }

</style>