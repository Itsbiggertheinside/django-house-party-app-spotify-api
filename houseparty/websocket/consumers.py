import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from core.models import Room
from .models import Player


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.current_room = self.scope['url_route']['kwargs']['room_code']
        self.current_room_group = f'room-{self.current_room}'

        await self.channel_layer.group_add(
            self.current_room_group, self.channel_name
        )

        print(self.current_room_group)

        await self.accept()


    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.current_room_group, self.channel_name
        )


    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        id = text_data_json['id']
        sender = text_data_json['sender']
        username = text_data_json['username']
        text = text_data_json['text']
        action = text_data_json['action']

        await self.channel_layer.group_send(
            self.current_room_group, {
                'type': 'chat_message',
                'id': id,
                'sender': sender,
                'text': text,
                'action': action
            }
        )

        await self.channel_layer.group_send(
            self.current_room_group, {
                'type': 'skip_vote',
                'username': username,
                'action': action
            }
        )


    async def chat_message(self, event):
        id = event['id']
        sender = event['sender']
        text = event['text']
        action = event['action']

        await self.send(text_data=json.dumps({
            'id': id,
            'sender': sender,
            'text': text,
            'action': action
        }))


    async def skip_vote(self, event):
        user_id = event['user_id']
        username = event['username']
        action = event['action']

        await self.create_skip_vote(self.current_room, user_id)

        await self.send(text_data=json.dumps({
            'user_id': user_id,
            'username': username,
            'action': action
        }))


    @database_sync_to_async
    def create_skip_vote(self, code, user_id):
        try:
            room = Room.objects.select_related('host__user', 'player').prefetch_related('player__skip_votes__user').get(code=code)
            if not user_id in room.player.skip_votes.all():
                room.player.skip_votes.add(user_id)
                room.save()
        except Exception as e:
            print(e)