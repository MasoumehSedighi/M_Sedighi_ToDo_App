from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'is_superuser', 'is_active']
    list_filter = ['email', 'is_superuser', 'is_active']
    search_fields = ('email',)
    ordering = ['-id',]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_superuser", "is_staff", "is_active"]}),
        ('group permissions', {'fields': ('groups', 'user_permissions')}),
        ("important_date", {"fields": ["last_login",]})
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]


admin.site.register(User,CustomUserAdmin)

