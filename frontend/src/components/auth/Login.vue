<template>
    <div id="login-panel" class="auth-panel-front">
        <b-card border-variant="dark">
            <b-card-body>
                <h2 class="mb-4">Giriş Yap</h2>
                <b-form>
                    <b-form-group label="Kullanıcı adı:" label-for="login-username">
                        <b-form-input id="login-username" required></b-form-input>
                    </b-form-group>
                    <b-form-group label="Kullanıcı şifresi:" label-for="login-password">
                        <b-form-input id="login-password" type="password" required></b-form-input>
                    </b-form-group>
                    <b-button variant="light">Giriş Yap</b-button>
                </b-form>
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