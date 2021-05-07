<template>
    <div id="auth">
        <b-container>
            <b-row align-h="around">
                <b-col md="4">
                    <b-img class="d-none d-md-block" fluid :src="require('../assets/images/cherry-sign-up.png')" />
                </b-col>
                <b-col md="4">
                    <b-button @click="handleChangeAuthMethod()" id="change-panel-button" variant="light">
                        <b-img fluid src="https://img.icons8.com/cotton/48/000000/double-right.png" />
                    </b-button>
                    <Login />
                    <Register />
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import Login from '../components/auth/Login.vue'
import Register from '../components/auth/Register.vue'

export default {
    name: 'Auth',
    components: {
        Login, Register
    },
    methods: {
        handleChangeAuthMethod() {
            const login_panel = document.getElementById('login-panel')
            const register_panel = document.getElementById('register-panel')
            
            if (login_panel.classList.contains('auth-panel-front')) {
                login_panel.className = 'auth-panel-back'
                register_panel.className = 'auth-panel-front'
            } else {
                login_panel.className = 'auth-panel-front'
                register_panel.className = 'auth-panel-back'
            }
        }
    },
    mounted() {
        this.$cookies.remove('token')
        this.$cookies.remove('username')
    }
}
</script>

<style>

    #auth {
        margin-top: 5rem;
    }

    #login-panel, #register-panel, #change-panel-button {
        position: absolute;
    }

    #change-panel-button {
        z-index: 3;
        transform: translate(10rem, -1.8rem);
    }

    .auth-panel-front {
        z-index: 2;
        transform: translateX(-15%);
    }

    .auth-panel-back {
        z-index: 1;
        transform: translate(15%, 5%) scale(.8);
        pointer-events: none;
        filter: blur(.1rem);
    }

</style>