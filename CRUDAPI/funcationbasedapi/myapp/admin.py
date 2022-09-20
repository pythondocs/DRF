from django.contrib import admin
from .models import StudentUser
# Register your models here.

@admin.register(StudentUser)
class AdminUser(admin.ModelAdmin):
    list_display = ['id','name', 'roll', 'city']
