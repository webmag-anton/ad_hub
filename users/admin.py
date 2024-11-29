# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    
    # Fields that will be displayed in the user list
    list_display = ('username', 'email', 'phone', 'avatar', 'is_staff', 'is_active', 'date_joined')
    
    # Fields by which you can search for users in the admin panel
    search_fields = ('username', 'email', 'phone')
    
    # Fields for filtering in the admin panel
    list_filter = ('is_staff', 'is_active', 'date_joined')
    
    # Fields that will be available when creating/editing a user
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'avatar')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'avatar', 'password1', 'password2'),
        }),
    )
    ordering = ('-date_joined',)

# Register a custom user model with a custom admin class
admin.site.register(User, CustomUserAdmin)
