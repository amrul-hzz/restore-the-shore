from django.db import models
from my_account.models import UserAccount

# Create your models here.
class Post(models.Model):
    creator = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=255)
    image = models.URLField()

class Comment(models.Model):
    creator = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=255)
    original_post = models.ForeignKey(Post, on_delete=models.CASCADE)