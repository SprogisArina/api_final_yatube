
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from api.mixins import PermissionMixin
from api.serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)
from posts.models import Group, Post


class PostViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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

    # get_queryset
    # router
    # сохранение при post запросе
