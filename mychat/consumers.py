from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.utils import timezone
from asgiref.sync import sync_to_async
from .models import Message
import json

User = get_user_model()


# ============================
# 🔵 CHAT CONSUMER
# ============================

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope["user"]
        self.other_username = self.scope["url_route"]["kwargs"]["username"]

        if self.user.is_anonymous:
            await self.close()
            return

        users = sorted([self.user.username, self.other_username])
        self.room_group_name = f"chat_{users[0]}_{users[1]}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Mark user online
        self.user.is_online = True
        self.user.last_seen = timezone.now()
        await sync_to_async(self.user.save)()

        # Broadcast presence
        await self.channel_layer.group_send(
            "online_users",
            {
                "type": "user_status",
                "user": self.user.username,
                "status": "online"
            }
        )

    async def disconnect(self, close_code):

        self.user.is_online = False
        self.user.last_seen = timezone.now()
        await sync_to_async(self.user.save)()

        await self.channel_layer.group_send(
            "online_users",
            {
                "type": "user_status",
                "user": self.user.username,
                "status": "offline"
            }
        )

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "").strip()

        if not message:
            return

        receiver = await sync_to_async(User.objects.get)(
            username=self.other_username
        )

        # Save message
        await sync_to_async(Message.objects.create)(
            sender=self.user,
            receiver=receiver,
            content=message
        )

        # Broadcast message
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": self.user.username,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "sender": event["sender"],
        }))
      

# ============================
# 🟢 PRESENCE CONSUMER
# ============================

class PresenceConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope["user"]

        if self.user.is_anonymous:
            await self.close()
            return

        await self.channel_layer.group_add(
            "online_users",
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "online_users",
            self.channel_name
        )

    async def user_status(self, event):
        await self.send(text_data=json.dumps({
            "user": event["user"],
            "status": event["status"]
        }))