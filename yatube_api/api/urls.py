from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

token_urlpetterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

v1_urlpetterns = [
    path('token/', include(token_urlpetterns)),
]

urlpatterns = [
    path('v1/', include(v1_urlpetterns))
]
