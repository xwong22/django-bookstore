from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Order (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bookID = models.ForeignKey("books.Book", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return "Order " + str(self.pk)
    
    def get_absolute_url(self):
        return reverse("orders:order-detail", kwargs={"pk":self.id})
