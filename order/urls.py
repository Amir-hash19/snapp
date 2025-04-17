from django.urls import path
from .views import RouteAPIView
from .views import TravelTimeView



urlpatterns = [
    path("route", RouteAPIView.as_view()),
    path('travel-time/', TravelTimeView.as_view(), name='travel-time'),
]
