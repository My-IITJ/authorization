import imp
from django.contrib import admin
from users.models import CustomUser
from users.models import UserRole

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'verification_status')

admin.site.register(CustomUser, UserAdmin)
admin.site.register(UserRole, UserRoleAdmin)
