from rest_framework import serializers
from .models import Client, Newsletter, Message


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    client_id = ClientSerializer(read_only=True)
    newsletter_id = NewsletterSerializer(read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
