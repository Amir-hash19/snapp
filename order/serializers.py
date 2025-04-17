from rest_framework.serializers import ModelSerializer, StringRelatedField
from account.models import Account
from .models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"