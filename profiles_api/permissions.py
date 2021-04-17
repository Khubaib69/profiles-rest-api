from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow Users To Edit Their Own Profile"""

    def has_object_permission(self,request,view,obj):
        """Check If The User Is Trying To Edit Their Own Profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.id==request.user.id
