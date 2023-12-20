from rest_framework import routers
from django.urls import include, path
from .views import ClientViewSet, NewsletterViewSet, SendView

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'newsletter', NewsletterViewSet)
# router.register(r'message', MessageViewSet)

# urlpatterns = router.urls

urlpatterns = [
    # path("https://probe.fbrq.cloud/v1/send/<int:msgId>", SendCreate.as_view()),
    path('', include(router.urls)),

    path('send/<int:msgId>', SendView.as_view(), name='send_data'),
]
