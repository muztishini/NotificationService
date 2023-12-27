from rest_framework import serializers
from .models import Client, Newsletter, Message
from datetime import datetime, timezone


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"

    def create(self, validated_data):
        newsletter = Newsletter.objects.create(**validated_data)

        start_date_time = validated_data.get("start_date_time")
        end_date_time = validated_data.get("end_date_time")
        now_date_time = datetime.now(timezone.utc)

        if now_date_time >= start_date_time.replace(tzinfo=timezone.utc) and now_date_time <= end_date_time.replace(
                tzinfo=timezone.utc):
            print("True")
            new_id = newsletter.id
            message_serializer = MessageSerializer(data=validated_data)
            if message_serializer.is_valid():
                message_serializer.save()
            MessageSerializer.create(self, new_id)
        elif start_date_time.replace(tzinfo=timezone.utc) > now_date_time:
            print("Future")
        else:
            print("False")
        return newsletter


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

    def create(self, new_id):
        creation_date_time = datetime.now(timezone.utc)
        newsletter_id = Newsletter.objects.get(pk=new_id)

        cofc = newsletter_id.client_filter_operator_code
        cft = newsletter_id.client_filter_tag

        clients = Client.objects.filter(mobile_operator_code=cofc, tag=cft).all()

        messages = []

        for cl_id in clients:
            client_id = Client.objects.get(pk=cl_id.id)
            message = Message.objects.create(client_id=client_id, newsletter_id=newsletter_id,
                                             creation_date_time=creation_date_time, send_status="send")
            messages.append(message)

        return messages
