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
    client_id = ClientSerializer()
    newsletter_id = NewsletterSerializer()

    class Meta:
        model = Message
        fields = "__all__"
