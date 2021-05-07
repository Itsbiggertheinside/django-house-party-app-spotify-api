<template>
    <div id="login-panel" class="auth-panel-front">
        <b-card border-variant="dark">
            <b-card-body>
                <h2 class="mb-4">Giriş Yap</h2>
                <h6 v-if="error != ''" style="color: #E12729">{{error}}</h6>
                <b-form-group class="mb-4" label="Kullanıcı adı:" label-for="login-username">
                    <b-form-input v-model="credentials.username" id="login-username" required></b-form-input>
                </b-form-group>
                <b-form-group class="mb-4" label="Kullanıcı şifresi:" label-for="login-password">
                    <b-form-input v-model="credentials.password" id="login-password" type="password" required></b-form-input>
                </b-form-group>
                <b-button @click="handleLogin(credentials)" variant="light">Giriş Yap</b-button>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    methods: {
        ...mapActions({login: 'login', setCurrentUser: 'setCurrentUser'}),
        async handleLogin(credentials) {
            await this.login(credentials)
            .then(async () => {
                await this.setCurrentUser()
                .then(status => {
                    if (status == 200) {
                        window.location.href = '/home'
                    } else {
                        this.error = 'Bir hata oluştu!'
                    }
                }).catch(err => console.log(err))
            }).catch(() => this.error = 'Giriş bilgilerin yanlış!')
        }
    },
    computed: {
        ...mapGetters({getToken: 'getToken', getKeyIsReturned: 'getKeyIsReturned'})
    },
    data() {
        return {
            credentials: {
                username: '',
                password: ''
            },
            error: ''
        }
    }
}
</script>

<style>

</style>