from api.permissions import OnlyAuthor, ReadOnly


class PermissionMixin:

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return (ReadOnly(),)
        return (OnlyAuthor(),)
