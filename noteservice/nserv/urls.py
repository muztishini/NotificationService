from rest_framework import routers
from .views import ClientViewSet, NewsletterViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'newsletter', NewsletterViewSet)
router.register(r'message', MessageViewSet)

urlpatterns = router.urls
