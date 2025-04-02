
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.mixins import PermissionMixin
from api.serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)
from posts.models import Group, Post, User


class PostViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(PermissionMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_post_id_from_url(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post, post_id

    def get_queryset(self):
        post, post_id = self.get_post_id_from_url()
        return post.comments.all()

    def perform_create(self, serializer):
        post, post_id = self.get_post_id_from_url()
        serializer.save(
            author=self.request.user,
            post_id=post_id
        )


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following',)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follows.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
