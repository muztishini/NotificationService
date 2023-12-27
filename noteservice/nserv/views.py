from rest_framework import viewsets
# from rest_framework.response import Response
from .serializers import ClientSerializer, NewsletterSerializer, MessageSerializer
from .models import Client, Newsletter, Message
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class StatsView(ListAPIView):
    serializer_class = NewsletterSerializer

    def get_queryset(self):
        queryset = Newsletter.objects.all()
        return queryset


class StatView(RetrieveAPIView):
    serializer_class = NewsletterSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        print(pk)
        queryset = Newsletter.objects.filter(id=pk)
        print(queryset)
        messages = Message.objects.filter(newsletter_id=pk).all()
        for mess in messages:
            print(mess.client_id)
            print(mess.send_status)
            print(mess.creation_date_time)
        # print(messages)
        return queryset

