from django.db import models


class Client(models.Model):
    phone_number = models.CharField(max_length=12)
    mobile_operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.id


class Newsletter(models.Model):
    start_date_time = models.DateTimeField()
    message_text = models.TextField()
    client_filter_operator_code = models.CharField(max_length=10)
    client_filter_tag = models.CharField(max_length=50)
    end_date_time = models.DateTimeField()

    # def __str__(self):
    #     return self.id


class Message(models.Model):
    creation_date_time = models.DateTimeField()
    send_status = models.CharField(max_length=50)
    newsletter_id = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.id
