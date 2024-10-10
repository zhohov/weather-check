from django.contrib import admin

from .models import UserLog


@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    list_filter = ["telegram_user_id"]
    search_fields = ["telegram_user_id", "user_command"]
    ordering = ["-timestamp"]

