from django.contrib import admin
from .models import User

@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    """Административная панель для модели User."""

    list_display = ('email', 'username', "first_name", "last_name", 'is_admin',)  # Список полей, отображаемых в списке записей
    list_filter = ('is_admin', 'email', 'username',)
    readonly_fields = (
        "last_login", "date_joined",)