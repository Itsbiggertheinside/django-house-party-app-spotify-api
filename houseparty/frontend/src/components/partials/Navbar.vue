<template>
    <div class="mb-4">
        <b-navbar type="dark" class="container">
            <b-navbar-nav class="d-flex w-100 justify-content-between">
                <div>
                    <b-nav-item @click="handleRoute('/home')">Home</b-nav-item>
                </div>

                <div class="d-flex justify-content-end">
                    <b-nav-item @click="handleRoute('/login')">Giriş Yap</b-nav-item>

                    <b-nav-item-dropdown text="Kullanıcı" right>
                        <b-dropdown-item href="#">Hesabım</b-dropdown-item>
                        <b-dropdown-item href="#">Ayarlar</b-dropdown-item>
                        <b-dropdown-item href="#">Çıkış Yap</b-dropdown-item>
                    </b-nav-item-dropdown>
                </div>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>

<script>
export default {
    methods: {
        handleRoute(link) {
            this.$router.push(link)
        }
    }
}
</script>

<style>

</style>