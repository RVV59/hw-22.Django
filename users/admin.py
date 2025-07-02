from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Убираем сортировку по username (которого нет)
    ordering = ('email',)  # Сортируем по email вместо username

    # Обновляем список полей в админке
    list_display = ('email', 'phone', 'country', 'is_staff')
    search_fields = ('email', 'phone', 'country')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('phone', 'country', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone', 'country'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)