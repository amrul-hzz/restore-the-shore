from django.db import models
from landing_page.models import UserAccount 
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # TODO
    # nanti ganti ke user account
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creator_name = models.CharField(max_length=255, default="Unknown")
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255)
    image = models.URLField()

class Comment(models.Model):
    # TODO
    # nanti gnati ke user account 
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creator_name = models.CharField(max_length=255, default="Unknown")
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255)
    original_post_id = models.PositiveIntegerField(default=0)