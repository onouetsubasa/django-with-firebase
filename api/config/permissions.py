from rest_framework import permissions


class IsLogedIn(permissions.BasePermission):

    def has_permission(self, request):
        return request.user and request.user.is_authenticated and not request.user.is_firebase_anonymous
