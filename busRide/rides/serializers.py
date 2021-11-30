
from rest_framework import serializers
from rides.models import *


class BusSerializer(serializers.ModelSerializer):

    licence_plate = serializers.CharField(max_length=6)
    year = serializers.IntegerField()
    brand = serializers.CharField(max_length=30)
    model = serializers.CharField(max_length=20)
    in_service = serializers.BooleanField()

    class Meta:
        model = Bus
        fields = ['licence_plate', 'year', 'brand', 'model', 'in_service']