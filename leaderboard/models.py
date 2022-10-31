from email.policy import default
from django.db import models
from landing_page.models import UserAccount

# Create your models here.
class LeaderBoard(models.Model):
    users = models.ForeignKey(UserAccount, on_delete=models.CASCADE, default=None)
    quote = models.TextField(default = "")