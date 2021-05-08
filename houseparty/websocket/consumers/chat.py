import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.current_room = self.scope['url_route']['kwargs']['code']
        self.current_room_group = f'room-{self.current_room}'

        await self.channel_layer.group_add(
            self.current_room_group, self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.current_room_group, self.channel_name
        )

    async def receive(self, text_data, bytes_data):
        text_data_json = json.loads(text_data)
        sender = text_data_json['sender']
        text = text_data_json['text']

        await self.channel_layer.group_send(
            self.current_room_group, {
                'type': 'chat_message',
                'sender': sender,
                'text': text,
            }
        )

    async def chat_message(self, event):
        sender = event['sender']
        text = event['text']

        await self.send(text_data=json.dumps({
            'sender': sender,
            'text': text
        }))