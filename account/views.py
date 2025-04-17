from .models import Account
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class CreateAccountView(CreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [AllowAny]
    
