from rest_framework import permissions


class OnlyAuthor(permissions.BasePermission):
    """Разрешение на изменение контента"""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
