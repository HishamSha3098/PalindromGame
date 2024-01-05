from django.db import models
import random
from django.contrib.auth.models import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.CharField(max_length=255, unique=True)
    string_value = models.CharField(max_length=255, default='')
    random_number = models.IntegerField(default=0)
