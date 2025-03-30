from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

token_urlpetterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

v1_router = routers.DefaultRouter()
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('follow', FollowViewSet, basename='follow')

v1_urlpetterns = [
    path('token/', include(token_urlpetterns)),
    path('', include(v1_router))
]

urlpatterns = [
    path('v1/', include(v1_urlpetterns))
]
