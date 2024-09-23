from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'password', 'last_login', 'is_superuser', 'is_staff','is_active', 'date_joined',)  # Поля для поиска
    filter_horizontal = ('groups','user_permissions')    

admin.site.register(User, UserAdmin)