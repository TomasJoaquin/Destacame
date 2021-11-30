from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rides.models import *
from rides.serializers import *

class BusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bus to be viewed or edited.
    """
    queryset = Bus.objects.all()
    serializer_class = BusSerializer