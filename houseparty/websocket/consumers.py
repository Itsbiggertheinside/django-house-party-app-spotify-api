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
        action_type = text_data_json['action_type']

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

        await self.channel_layer.group_send(
            self.current_room_group, {
                'type': 'set_listener',
                'username': username,
                'action_type': action_type,
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


    async def set_listener(self, event):
        user_id = event['user_id']
        username = event['username']
        action_type = event['action_type']
        action = event['action']

        if action_type == 'add':
            await self.set_room_listener(self.current_room, user_id, 'increase')
        elif action_type == 'remove':
            await self.set_room_listener(self.current_room, user_id, 'decrease')

        await self.send(text_data=json.dumps({
            'user_id': user_id,
            'username': username,
            'action': action
        }))


    @database_sync_to_async
    def create_skip_vote(self, code, user_id):
        try:
            room = Room.objects.select_related('host__user', 'player', 'listener').prefetch_related('player__skip_votes__user', 'listener__active_users__user').get(code=code)
            if not user_id in room.player.skip_votes.all():
                room.player.skip_votes.add(user_id)
                room.save()
        except Exception as e:
            print(e)


    @database_sync_to_async
    def set_room_listener(self, code, user_id, action):
        try:
            room = Room.objects.select_related('host__user', 'player', 'listener').prefetch_related('player__skip_votes__user', 'listener__active_users__user').get(code=code)

            if action == 'increase':
                if not user_id in room.listener.active_users.all():
                    room.listener.active_users.add(user_id)
                    room.save()
            elif action == 'decrease':
                if user_id in room.listener.active_users.all():
                    room.listener.active_users.remove(user_id)
                    room.save()

        except Exception as e:
            print(e)