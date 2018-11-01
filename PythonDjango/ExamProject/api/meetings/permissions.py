from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsPrivate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.is_private is False or request.user == obj.author
