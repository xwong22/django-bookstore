from django.urls import path
from .views import ( 
    RequestedbookListView,
    # RequestedbookDetailView,
    RequestedbookCreateView,
    RequestedbookDeleteView
) 

app_name = 'requestedbook'
urlpatterns = [
    path('', RequestedbookListView.as_view(), name='requestedbook-list'),
    # path('<int:pk>/', RequestedbookDetailView.as_view(), name='requestedbook-detail'),
    path('create/', RequestedbookCreateView, name='requestedbook-create'),
    path('<int:pk>/delete/', RequestedbookDeleteView.as_view(), name='requestedbook-delete'),
]