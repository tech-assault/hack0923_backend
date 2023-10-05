from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group, Permission

from sales.models import Sale, Store, Forecast, Category


admin_group, created = Group.objects.get_or_create(name='Администраторы')
user_group, created = Group.objects.get_or_create(name='Пользователи')

admin_permissions = Permission.objects.filter(content_type__app_label='sales', content_type__model='store')
admin_group.permissions.set(admin_permissions)

view_store_permission = Permission.objects.get(content_type__app_label='sales', content_type__model='store', codename='view_store')
user_group.permissions.add(view_store_permission)

admin_group.save()
user_group.save()

admin.site.unregister(Group)  
admin.site.register(Group)

@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    """Административная панель для модели User."""

    list_display = ('email', 'username', "first_name", "last_name", 'is_admin',)  # Список полей, отображаемых в списке записей
    list_filter = ('is_admin', 'email', 'username',)
    readonly_fields = (
        "last_login", "date_joined",)


