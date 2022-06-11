from rest_framework.permissions import BasePermission

class GroupPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user.groups)
        if request.user.groups.filter(name='developers').exists():

            return True
        return False