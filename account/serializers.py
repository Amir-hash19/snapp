from rest_framework.serializers import ModelSerializer, StringRelatedField
from account.models import Account



class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

