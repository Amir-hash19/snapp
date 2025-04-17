from rest_framework.serializers import ModelSerializer, StringRelatedField
from account.models import Account
from .models import Order
from rest_framework import serializers


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"




class RouteRequestSerializer(serializers.Serializer):
    origin_lat = serializers.FloatField()
    origin_lng = serializers.FloatField()
    dest_lat = serializers.FloatField()
    dest_lng = serializers.FloatField()        




class TravelTimeSerializer(serializers.Serializer):
    origin = serializers.CharField(help_text="مثال: 35.7448,51.3751")
    destination = serializers.CharField(help_text="مثال: 35.7325,51.4221")
    type = serializers.ChoiceField(choices=['car', 'motorcycle', 'pedestrian'], default='car')    