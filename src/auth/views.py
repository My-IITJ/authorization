from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import UserRole
# Create your views here.
from .serializers import UserSerializer
from rest_framework import viewsets

from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = UserRole.objects.all()
    serializer_class = UserSerializer