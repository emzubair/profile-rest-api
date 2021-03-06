from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to edit their own users"""

    def has_object_permission(self,request,view,obj):
        """Checks if user is trying to edit his/her own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Checks if user is trying to update his/her own feed"""

    def has_object_permission(self,request,view,obj):
        """Checks if user is trying to update his/her own feed"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
