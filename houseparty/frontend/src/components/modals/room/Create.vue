<template>
    <div>
        <b-modal id="room-create-modal" ref="room-create-modal" centered>

            <template #modal-header>
                <h5 class="m-0">Bir oda oluştur</h5>
                <b-button @click="hideRoomCreateModal()" class="modal-close-button"><b-icon-x></b-icon-x></b-button>
            </template>

            <p class="mt-2 mb-3">Oluşturmak istediğiniz oda için eşsiz bir kod tanımlayın:</p>
            <b-form-input v-model="code" class="mt-3 mb-4" autocomplete="off"></b-form-input>

            <div class="d-flex justify-content-between align-items-center mb-2">
                <h6 class="m-0">Kullanıcılar şarkıyı durdurabilir mi?</h6>
                <b-button @click="handleCheckboxSubmit('guest_can_pause', 'pause')" v-model="guest_can_pause" ref="guest_can_pause" class="checkbox-button" style="background-color: #E12729"><b-icon-x></b-icon-x></b-button>
            </div>

            <div class="d-flex justify-content-between align-items-center mb-2">
                <h6 class="m-0">Odayı kilitlemek ister misin?</h6>
                <b-button @click="handleCheckboxSubmit('is_locked', 'lock')" ref="is_locked" class="checkbox-button" style="background-color: #E12729"><b-icon-x></b-icon-x></b-button>
            </div>
            
            <b-form-input type="password" v-show="is_locked" class="my-1" placeholder="Parola gir"></b-form-input>

            <div class="d-flex justify-content-between align-items-center mb-2">
                <h6 class="m-0">Şarkıyı geçmek için şu kadar oya ihtiyaç var:</h6>
                <b-button v-show="votes_to_skip_button" @click="handleShowVotesToSkip()" class="checkbox-button" style="background-color: #E12729"><b-icon-question></b-icon-question></b-button>
                <b-form-input v-model="votes_to_skip_count" v-show="show_votes_to_skip_count_input" class="create-modal-input"></b-form-input>
            </div>

            <template #modal-footer>
                <b-button @click="handleCreateRoom()" class="panel-button"><b-icon-check></b-icon-check></b-button>
            </template>

        </b-modal>
    </div>
</template>

<script>
import { mapActions } from 'vuex'


export default {
    methods: {
        ...mapActions({createRoom: 'createRoom'}),
        hideRoomCreateModal() {
            this.$refs['room-create-modal'].hide()
        },
        handleShowVotesToSkip() {
            this.show_votes_to_skip_count_input = !this.show_votes_to_skip_count_input
            this.votes_to_skip_button = !this.votes_to_skip_button
        },
        handleCheckboxSubmit(ref, type) {
            if (!this.$refs[ref].classList.contains('clicked')) {
                this.$refs[ref].classList.add('clicked')
                this.$refs[ref].innerHTML = `<svg viewBox="0 0 16 16" width="1em" height="1em" focusable="false" role="img" aria-label="check" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi-check b-icon bi"><g><path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"></path></g></svg>`
                this.$refs[ref].style.backgroundColor = '#346E93'
            } else {
                this.$refs[ref].classList.remove('clicked')
                this.$refs[ref].innerHTML = `<svg viewBox="0 0 16 16" width="1em" height="1em" focusable="false" role="img" aria-label="x" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi-x b-icon bi"><g><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"></path></g></svg>`
                this.$refs[ref].style.backgroundColor = '#E12729'
            }

            if (type == 'lock' && this.is_locked == true) {
                this.is_locked = false
            } else if (type == 'lock' && this.is_locked == false) {
                this.is_locked = true
            }
        },
        async handleCreateRoom() {
            let settings = {
                code: this.code,
                is_locked: this.is_locked,
                guest_can_pause: this.guest_can_pause,
                votes_to_skip_count: this.votes_to_skip_count
            }

            await this.createRoom(settings)
            .then(status => {
                if (status == 201) {
                    this.hideRoomCreateModal()
                    this.$router.push('/room/' + this.code)
                } else {
                    console.log('Bir sorun oluştu')
                }
            })
        }
    },
    data() {
        return {
            votes_to_skip_button: true,
            show_votes_to_skip_count_input: false,

            code: '',
            is_locked: false,
            guest_can_pause: false,
            votes_to_skip_count: 0
        }
    }
}
</script>

<style>

</style>