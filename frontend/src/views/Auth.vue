<template>
    <div id="auth">
        <b-container>
            <b-row align-h="around">
                <b-col md="4">
                    <b-img fluid :src="require('../assets/images/cherry-sign-up.png')" />
                </b-col>
                <b-col md="4">
                    <b-button id="change-panel-button" variant="outline-light">
                        <b-img fluid src="https://img.icons8.com/cotton/64/000000/double-right.png" />
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
        transform: translate(7.5rem, -2.4rem);
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