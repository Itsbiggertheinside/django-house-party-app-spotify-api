<template>
    <div>
        <b-modal v-model="show" centered>

            <template #modal-header>
                <h5 class="m-0">Sistem Mesajı</h5>
                <b-button @click="show = !show" class="modal-close-button"><b-icon-x></b-icon-x></b-button>
            </template>

            <p class="mt-2 mb-3">{{system_info.message}}</p>

            <template #modal-footer>
                <b-button @click="show = !show" class="panel-button"><b-icon-check></b-icon-check></b-button>
            </template>

        </b-modal>
    </div>
</template>

<script>
export default {
    props: ['system_info'],
    methods: {
    },
    data() {
        return {
            show: false
        }
    },
    mounted() {
        this.show = this.system_info.is_visible
    }
}
</script>

<style>

</style>