from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from redis.client import Redis


class DrawingConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'drawing_%s' % self.room_name

        # 그림 데이터를 저장할 Redis 클라이언트 연결
        self.redis = Redis(host='localhost', port=6379, db=0)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']

        if message_type == 'chat':
            self.handle_chat(text_data_json)

        elif message_type == 'draw':
            self.handle_draw(text_data_json)

    # Receive chat message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))

    # Receive draw message from room group
    def draw_message(self, event):
        data = event['data']

        # Save draw data to Redis
        self.redis.set(self.room_group_name, json.dumps(data))

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'draw',
            'data': data
        }))

    # Handle chat message
    def handle_chat(self, text_data_json):
        message = text_data_json['message']

        # Send chat message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Handle draw message
    def handle_draw(self, text_data_json):
        data = text_data_json['data']

        # Send draw message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'draw_message',
                'data': data
            }
        )
