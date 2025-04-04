from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowList, GroupViewSet, PostViewSet


v1_router = routers.DefaultRouter()
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
v1_router.register('posts', PostViewSet, basename='posts')

v1_urlpatterns = [
    path('follow/', FollowList.as_view()),
    path('', include('djoser.urls.jwt')),
    path('', include(v1_router.urls))
]

urlpatterns = [
    path('v1/', include(v1_urlpatterns))
]
