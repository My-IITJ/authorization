from auth.serializers import *
from auth.views import UserViewSet, signup, signin, signout
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView


router = DefaultRouter()
# router.register(r'signup', UserViewSet, basename='Users')
# router.register(r'signin', UserViewSet, basename='User')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('signup/', signup),
    path('signin/',signin),
    path('signout/',signout),
    path('register', RegisterView.as_view())
]