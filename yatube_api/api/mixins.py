from api.permissions import OnlyAuthor, ReadOnly


class PermissionMixin:

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return (OnlyAuthor(),)
