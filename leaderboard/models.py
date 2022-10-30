from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from landing_page.models import UserAccount

# Create your models here.
class LeaderBoard(models.Model):
    users = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    quote = models.TextField()