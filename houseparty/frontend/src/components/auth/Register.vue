<template>
    <div id="register-panel" class="auth-panel-back">
        <b-card border-variant="dark">
            <b-card-body>
                <h2 class="mb-4">Kayıt Ol</h2>
                <b-form-group class="mb-4" label="Kullanıcı adı:" label-for="register-username">
                    <b-form-input id="register-username" required></b-form-input>
                </b-form-group>
                <b-form-group class="mb-4" label="Kullanıcı şifresi:" label-for="register-password">
                    <b-form-input id="register-password" type="password" required></b-form-input>
                </b-form-group>
                <b-form-group class="mb-4" label="Şifre tekrarı:" label-for="register-password-confirm">
                    <b-form-input id="register-password-confirm" type="password" required></b-form-input>
                </b-form-group>
                <b-button variant="light">Kayıt Ol</b-button>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>