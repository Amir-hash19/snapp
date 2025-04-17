from rest_framework.generics import CreateAPIView, ListAPIView
from order.serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Order
from account.models import Account




