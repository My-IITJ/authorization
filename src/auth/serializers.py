import email
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.hashers import make_password
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,style={'input_type': 'password'})
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name','last_name','password']
    
    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user