from authapp.serializers import *
from authapp.views import UserViewSet, signup, signin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from authapp.apis import GoogleLoginApi, LogoutApi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
# router.register(r'signup', UserViewSet, basename='Users')
# router.register(r'signin', UserViewSet, basename='User')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('signup/', signup),
    path('signin/',signin),
    path('signin/google/', GoogleLoginApi.as_view(), name='login-with-google'),
    path('signout/', LogoutApi.as_view(), name='logout'),
]
