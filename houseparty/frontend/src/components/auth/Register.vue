<template>
    <div id="register-panel" class="auth-panel-back">
        <b-card border-variant="dark">
            <b-card-body>
                <h2 class="mb-4">Kayıt Ol</h2>
                <h6 v-if="error != ''" variant="danger">{{error}}</h6>
                <b-form-group class="mb-4" label="Email adresi:" label-for="register-email">
                    <b-form-input v-model="credentials.email" id="register-email" required></b-form-input>
                </b-form-group>
                <b-form-group class="mb-4" label="Kullanıcı adı:" label-for="register-username">
                    <b-form-input v-model="credentials.username" id="register-username" required></b-form-input>
                </b-form-group>
                <b-form-group class="mb-4" label="Kullanıcı şifresi:" label-for="register-password">
                    <b-form-input v-model="credentials.password1" id="register-password" type="password" required></b-form-input>
                </b-form-group>
                <b-form-group class="mb-4" label="Şifre tekrarı:" label-for="register-password-confirm">
                    <b-form-input v-model="credentials.password2" id="register-password-confirm" type="password" required></b-form-input>
                </b-form-group>
                <b-button @click="handleRegister(credentials)" variant="light">Kayıt Ol</b-button>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    methods: {
        ...mapActions({register: 'register', setCurrentUser: 'setCurrentUser'}),
        async handleRegister(credentials) {
            await this.register(credentials)
            .then(async () => {
                await this.setCurrentUser()
                .then(() => {
                    window.location.href = '/home'
                }).catch(err => console.log(err))
            }).catch(err => console.log(err))
        }
    },
    computed: {
        ...mapGetters({getToken: 'getToken'})
    },
    data() {
        return {
            credentials: {
                email: '',
                username: '',
                password1: '',
                password2: '',
            },
            error: ''
        }
    }
}
</script>

<style>

</style>