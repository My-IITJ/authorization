from auth.serializers import *
from auth.views import UserViewSet, signup
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'signup', UserViewSet, basename='Users')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('signup/', signup)
]