from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# from create_event import models as eventModels


# Create your models here.
class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_point = models.IntegerField()
    # import models dari Event
    events_joined = ArrayField()  # ArrayField(eventModels.Event.objects)
    # atau Event punya ArrayField yang isinya nama participant biar bisa cek dari database langsung terus di filter
    # post di forum yang author nya user ini bisa langsung cek dari database forum aja

