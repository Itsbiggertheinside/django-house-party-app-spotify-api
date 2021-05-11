<template>
    <div>
        <b-card text-variant="white">
            <template #header>
                <div class="d-flex justify-content-between align-items-center">
                    <div class="d-flex align-items-center">
                        <b-avatar></b-avatar>
                        <h6 class="m-0">{{current_user}}</h6>
                    </div>
                    <b-avatar-group size="2rem" v-b-tooltip.hover.bottom :title="listener_count + ' aktif dinleyen'">
                        <b-avatar v-for="listener in listeners" :key="listener.user_id" src="https://placekitten.com/300/300" variant="info"></b-avatar>
                    </b-avatar-group>
                </div>
            </template>
            <b-card-body class="w-100" id="chat-panel">
                <div v-for="message in messages" :key="message.id" class="d-flex align-items-center">
                    <b-avatar></b-avatar>
                    <p class="m-0">{{message.sender}}: {{message.text}}</p>
                </div>
            </b-card-body>
            <template #footer>
                <b-form-input v-model="message_data.text" @keyup.enter="handleSendMessage(message_data)" class="chat-message-input"></b-form-input>
            </template>
        </b-card>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    props: ['listeners'],
    methods: {
        ...mapActions({sendMessage: 'sendMessage'}),
        handleSendMessage(data) {
            if (data.text != '') {
                this.sendMessage(data)
                this.message_data.text = ''
            }
        },
        handleScroll() {
            const chat_panel = document.querySelector('#chat-panel')
            chat_panel.scrollTop = chat_panel.scrollHeight
        }
    },
    computed: {
        ...mapGetters({messages: 'getMessages'})
    },
    data() {
        return {
            current_user: this.$cookies.get('username'),
            message_data: {
                code: this.$route.params.code,
                text: ''
            },
            listener_count: this.listeners.length
        }
    },
    watch: {
        messages: function () {
            this.handleScroll()
        }
    },
    mounted() {
        this.handleScroll()
    }
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