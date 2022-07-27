# we want users to update their own profiles only
# Users can see other profiles but can update their own profile only

from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:      # safe methods are : GET (Users can see other user profiles)
            return True
        return obj.id == request.user.id
        # NOTE: request.user.id is the authenticated id which should match with the object which we are updating
        # Now we have create our own permission class so configure our viewset to use this permission