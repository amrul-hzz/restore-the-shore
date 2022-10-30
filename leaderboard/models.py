from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LeaderBoard(models.Model):
    search = models.CharField(max_length = 255)