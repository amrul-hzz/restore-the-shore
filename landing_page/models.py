from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
#from create_event.models import Event

# Create your models here.
class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_point = models.IntegerField(default = 0)
    username = models.CharField(max_length = 63)
    # import models dari Event
    #events_joined = models.ManyToManyField(Event)

    # post di forum yang author nya user ini bisa langsung cek dari database forum aja

class Feedback(models.Model):
    message = models.TextField()