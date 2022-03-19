from django.shortcuts import render
from users.models import CustomUser 
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import generics
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import GenericAPIView
from .serializers import UserRegister
from rest_framework import status

class RegisterView(GenericAPIView):
    serializer_class = UserRegister

    def post(self, request):
        serializer = UserRegister(data=request.data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

@api_view(['POST'])
def signup(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"New User Created","data":serializer.data},status=201)
    else:
        return Response({"message":"Invalid data passed"})

@api_view(['POST'])
def signin(request):
    data = request.data
    username= data['username']
    password = data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return Response({"message":"User authenticated","data":{'username':username}},status=200)
        else:
           return Response({"message":"Invalid credentials"},status=400)
    else:
       return Response({"message":"User does not exist"},status=400)
   
@api_view(['POST','GET'])
def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({"message":"User logged out"},status=200,data=request.user)
    else:
        return Response({"message":"User not authenticated"},status=400)
    
            