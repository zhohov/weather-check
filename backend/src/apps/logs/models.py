from django.db import models


class UserLog(models.Model):
    telegram_user_id = models.IntegerField(verbose_name="Telegram User ID")
    user_command = models.CharField(verbose_name="User command", max_length=255)
    bot_response = models.TextField(verbose_name="Response from bot")
    timestamp = models.DateTimeField(verbose_name="Time", auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['telegram_user_id'])
        ]

    def __str__(self) -> str:
        return f"{self.telegram_user_id}, {self.user_command}, {self.timestamp}"

