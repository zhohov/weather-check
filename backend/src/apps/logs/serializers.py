from rest_framework import serializers

from .models import UserLog


class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = ["telegram_user_id", "user_command", "bot_response"]

