from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView
from django.urls import path


urlpatterns = [
    path("take-token/", TokenObtainPairView.as_view()),
    path("refresh-token/", TokenRefreshView.as_view()),
    path("verify-token/", TokenVerifyView.as_view()),

]
