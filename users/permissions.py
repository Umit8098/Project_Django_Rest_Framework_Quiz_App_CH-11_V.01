from rest_framework.permissions import BasePermission

class IsOwnerOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return bool(request.user.is_staff or request.user == obj.user)
