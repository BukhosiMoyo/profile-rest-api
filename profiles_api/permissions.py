from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """"This will allow users to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """This will check if the user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """This will allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """This will check if the user is trying to update thie own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id