from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    GENRE_CHOICES = (
        ("HORROR", "Horror"),
        ("ROMANCE", "Romance"),
        ("ADVENTURE", "Adventure")
    )

    bookname = models.CharField(max_length=300)
    isbn = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publishedDate = models.DateField()
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES)
    photoURL = models.CharField(max_length=400, default="https://demo.publishr.cloud/assets/common/images/edition_placeholder.png")
    quantityLeft = models.IntegerField()

    def __str__(self):
        return self.bookname

    def get_absolute_url(self):
        return reverse("books:book-detail", kwargs={"pk":self.id})
