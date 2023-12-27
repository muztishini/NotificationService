from rest_framework import viewsets
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
        unique_count = Message.objects.values('newsletter_id').distinct()
        lst = []
        for i in range(len(unique_count)):
            lst.append(unique_count[i]['newsletter_id'])
        lst_m = []
        for i in lst:
            lst_m.append(Message.objects.filter(newsletter_id=i).order_by("send_status"))

        data_report = {}
        i = 1
        j = 0
        for mess in lst_m:
            for item in mess:
                client_report = {"newsletter": lst[j],
                                 "client_id": item.id,
                                 "message_status": item.send_status,
                                 "message_creation_date_time": item.creation_date_time.strftime("%Y-%m-%d %H:%M:%S")}
                data_report[i] = client_report
                i += 1
            j += 1
        print(data_report)
        return queryset


class StatView(RetrieveAPIView):
    serializer_class = NewsletterSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Newsletter.objects.filter(id=pk)
        messages = Message.objects.filter(newsletter_id=pk).all()

        data_report = {}
        i = 1
        for mess in messages:
            client_report = {"client_id": mess.client_id.id,
                             "client_phone_number": mess.client_id.phone_number,
                             "message_status": mess.send_status,
                             "message_creation_date_time": mess.creation_date_time.strftime("%Y-%m-%d %H:%M:%S")}
            data_report[i] = client_report
            i += 1
        print(data_report)
        return queryset
