from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('email', 'username', 'is_online', 'last_seen', 'is_staff')
    list_filter = ('is_online', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('Online Status', {
            'fields': ('is_online', 'last_seen'),
        }),
    )