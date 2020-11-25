from django.db import models
from django.contrib.auth.models import User


class UserStats:
    user = models.OneToOneField(User, on_delete=models.SET_NULL)
    wins_count = models.IntegerField(default=0)
    losses_count = models.IntegerField(default=0)
