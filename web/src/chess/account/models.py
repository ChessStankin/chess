from django.db import models
from django.contrib.auth.models import User
from secrets import token_hex
from datetime import datetime, timedelta


class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    wins_count = models.IntegerField(default=0)
    losses_count = models.IntegerField(default=0)


class AuthJWT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    token = models.CharField(max_length=64, default=token_hex(32))
    expires_at = models.DateTimeField(default=datetime.now() + timedelta(days=7))

    def is_expired(self):
        if datetime.now() >= self.expires_at:
            return True
        return False

    def refresh(self):
        self.token = token_hex(32)
        self.expires_at = datetime.now() + timedelta(days=7)
        self.save()
