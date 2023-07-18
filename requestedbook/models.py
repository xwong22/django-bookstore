from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Requestedbook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    RBName = models.CharField(max_length=50)
    RBAuthor = models.CharField(max_length=50)
    Quantity =models.IntegerField(default=1)

    def get_absolute_url(self):
        return reverse("requestedbook:requestedbook-list")
