from django.db import models
from my_account.models import UserAccount

# Create your models here.
class Post(models.Model):
    poster = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/')