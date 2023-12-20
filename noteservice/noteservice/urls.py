from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# from noteservice.nserv.views import SendCreate

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('nserv.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # path("https://probe.fbrq.cloud/v1/send/<int:msgId>", SendCreate.as_view()),
]
