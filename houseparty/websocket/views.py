from rest_framework import generics, views, status
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from core.models import Room


# Create your views here.
class WebSocketHandler(views.APIView):
    
    def post(self, request, *args, **kwargs):
        action = request.data['action']
        code = request.data['code']
        data = {}


        if action == 'chat':
            data = {
                'type': 'chat_message',
                'id': str(request.data['id']),
                'sender': str(request.user.username),
                'text': str(request.data['text'].strip()),
                'action': str(action)
            }

        elif action == 'vote':
            data = {
                'type': 'skip_vote',
                'user_id': str(request.user.pk),
                'username': str(request.user.username),
                'action': str(action)
            }


        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(f'room-{code}', data)
        return Response(data, status=status.HTTP_201_CREATED)