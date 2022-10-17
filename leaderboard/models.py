from curses import use_default_colors
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# TODO: migrate the models

class Leaderboard(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.FloatField()
    date_joined = models.CharField(max_length=63)
