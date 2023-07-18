from django.db import models
from django.urls import reverse
from django.conf import settings


#https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    bookID = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    publishedDate = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("comments:comment-list")
    