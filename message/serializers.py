from rest_framework.serializers import ModelSerializer

from message.models import Chat_room, Message

class Chat_roomSerializer(ModelSerializer):
    model = Chat_room
    fields = '__all__'

class MessageSerializer(ModelSerializer):
    model = Message
    fields = '__all__'