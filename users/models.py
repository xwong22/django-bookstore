from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="profile",null=True)
    phone_number = models.CharField(max_length=11,null=True)
    address = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.user.username + "'s Profile"