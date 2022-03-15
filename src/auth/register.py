from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegister(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255, min_length=4),
    role = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['email', 'role'
                  ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
