import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import *





class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        
        
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        event = {
            'type': 'send_message',
            'message': message,
            'sender':self.channel_name
        }

        await self.channel_layer.group_send(self.room_name, event)

    async def send_message(self, event):
        data = event['message']
        sender_channel = event["sender"]
        
        if self.channel_name == sender_channel:
            await self.create_message(data=data)
        response_data = {
            'sender': data['sender'],
            'message': data['message'],
            'profile_picture': data['profilePic'],
        }
        await self.send(text_data=json.dumps({'message': response_data}))

    @database_sync_to_async
    def create_message(self, data):
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        sender_profile = Profile.objects.get(user__id=data['sender']['id'])
        new_message = Message(room=get_room_by_name, sender=sender_profile, message=data['message'])
        new_message.save()