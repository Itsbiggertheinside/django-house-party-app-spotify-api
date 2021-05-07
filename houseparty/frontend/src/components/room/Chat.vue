<template>
    <div>
        <b-card text-variant="white">
            <template #header>
                <div class="d-flex justify-content-between align-items-center">
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <h6 class="m-0">anothermayk</h6>
                    </div>
                    <b-avatar-group size="2rem" v-b-tooltip.hover.bottom title="15 aktif dinleyen">
                        <b-avatar src="https://placekitten.com/300/300" variant="info"></b-avatar>
                        <b-avatar src="https://placekitten.com/320/320" variant="dark"></b-avatar>
                        <b-avatar src="https://placekitten.com/300/300" variant="info"></b-avatar>
                        <b-avatar src="https://placekitten.com/320/320" variant="dark"></b-avatar>
                        <b-avatar src="https://placekitten.com/300/300" variant="info"></b-avatar>
                        <b-avatar src="https://placekitten.com/320/320" variant="dark"></b-avatar>
                    </b-avatar-group>
                </div>
            </template>
            <b-card-body id="chat-panel">
                <div class="w-100">
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex justify-content-end align-items-center">
                        <p class="m-0">Test mesaj</p>
                        <b-avatar></b-avatar>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex justify-content-end align-items-center">
                        <p class="m-0">Test mesaj</p>
                        <b-avatar></b-avatar>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex justify-content-end align-items-center">
                        <p class="m-0">Test mesaj</p>
                        <b-avatar></b-avatar>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex justify-content-end align-items-center">
                        <p class="m-0">Test mesaj</p>
                        <b-avatar></b-avatar>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex justify-content-end align-items-center">
                        <p class="m-0">Test mesaj</p>
                        <b-avatar></b-avatar>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                    <div class="d-flex justify-content-end align-items-center">
                        <p class="m-0">Test mesaj</p>
                        <b-avatar></b-avatar>
                    </div>
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <p class="m-0">Test mesaj</p>
                    </div>
                </div>
            </b-card-body>
            <template #footer>
                <b-form-input class="chat-message-input"></b-form-input>
            </template>
        </b-card>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>

    .card {
        filter: drop-shadow(.2rem .2rem .5rem #163c5f93);
        background-color: #31739c9d;
    }

    .chat-message-input {
        color: white;
        font-weight: 500;
        background-color: #184d6ed3;
    }

</style>