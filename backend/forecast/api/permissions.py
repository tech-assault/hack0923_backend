from rest_framework import permissions


class UserIsStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        # Проверяем, имеет ли пользователь доступ к магазину
        store = view.get_object()
        user = request.user
        return store.users.filter(id=user.id).exists()