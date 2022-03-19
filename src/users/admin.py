import imp
from django.contrib import admin
from users.models import CustomUser
from users.models import UserRole

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    exclude = ('jwt_token',)

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'verification_status')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserRole, UserRoleAdmin)
