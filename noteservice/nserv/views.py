from rest_framework import viewsets, status
# from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .serializers import ClientSerializer, NewsletterSerializer, MessageSerializer
from .models import Client, Newsletter, Message


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

#
# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer


# class SendCreate(ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

    # def perform_create(self, serializer):
    #     author = get_object_or_404(Message, id=self.request.data.get('msgId'))
    #     return serializer.save(author=author)

class SendView(APIView):
    def post(self, request, msgId):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            # отправляем POST-запрос
            response = requests.post(f'https://probe.fbrq.cloud/v1/send/{msgId}', data=data)
            return Response(response.json(), status=response.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def send_request(msg_id):
    #     url = f"https://probe.fbrq.cloud/v1/send/{msg_id}"
    #     payload = {
    #                 "id": 0,
    #                 "phone": 0,
    #                 "text": "string"
    #                 }  # Ваше тело запроса

    #     response = requests.post(url, json=payload)

    #     if response.status_code == 200:
    #         # Обработка успешного ответа
    #         print("Запрос успешно выполнен.")
    #     else:
    #         # Обработка ошибки
    #         print(f"Произошла ошибка при выполнении запроса. Код ошибки: {response.status_code}")
