from rest_framework import routers
from django.urls import include, path
from .views import ClientViewSet, NewsletterViewSet, MessageViewSet, StatsView, StatView

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'newsletter', NewsletterViewSet)
router.register(r'message', MessageViewSet)

# urlpatterns = router.urls

urlpatterns = [
    # path("https://probe.fbrq.cloud/v1/send/<int:msgId>", SendCreate.as_view()),
    path('', include(router.urls)),

    path('stat/', StatsView.as_view(), name='stats_data'),
    path('stat/<int:pk>', StatView.as_view(), name='stat_data'),
]
