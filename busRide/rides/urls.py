from rest_framework import routers
from django.urls import path, include
from rides import views

router = routers.DefaultRouter()

router.register(r'buses', views.BusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]