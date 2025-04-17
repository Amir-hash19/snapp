from rest_framework.generics import CreateAPIView, ListAPIView
from order.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Order
from account.models import Account
from rest_framework.views import APIView
from rest_framework import status
from order.serializers import RouteRequestSerializer
from .utils import get_route_from_neshan
from rest_framework.response import Response
import requests
from .serializers import TravelTimeSerializer



class RouteAPIView(APIView):
    def post(self, request):
        serializer = RouteRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            result = get_route_from_neshan(
                origin_lat=data['origin_lat'],
                origin_lng=data['origin_lng'],
                dest_lat=data['dest_lat'],
                dest_lng=data['dest_lng']
            )
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






from rest_framework.permissions import AllowAny
from django.db.models import Q
from .serializers import TravelTimeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class TravelTimeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TravelTimeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        origin = serializer.validated_data['origin']
        destination = serializer.validated_data['destination']
        route_type = serializer.validated_data['type']

        headers = {
            'Api-Key': 'service.00d6c8fd4c004cda990a8c2292faa271'
        }
        url = 'https://api.neshan.org/v4/direction'
        params = {
            'origin': origin,
            'destination': destination,
            'type': route_type
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()

            duration_seconds = int(data['routes'][0]['legs'][0]['duration']['value'])
            duration_text = data['routes'][0]['legs'][0]['duration']['text']

            
            final_price = (duration_seconds // 60) * 80

           
            if request.user.is_authenticated:
                user = request.user
                if hasattr(user, 'account'):
                    if user.account.wallet < final_price:
                        return Response({
                            'message': 'money not enough!',
                            'required_amount': final_price,
                            'wallet': user.account.wallet
                        }, status=status.HTTP_402_PAYMENT_REQUIRED)

            return Response({
                'origin': origin,
                'destination': destination,
                'type': route_type,
                'duration_seconds': duration_seconds,
                'duration_text': duration_text,
                'final_price': final_price
            })

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
