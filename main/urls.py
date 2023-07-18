from django.urls import path

from .views import homeView

app_name = "main"
urlpatterns = [
    path("", homeView, name="home"),
]